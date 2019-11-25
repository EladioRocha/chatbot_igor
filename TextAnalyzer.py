from textblob import TextBlob
import numpy, random, nltk, json

##### OUR MODULES #####
from training_model import model, stemmer, labels, words, data

class TextAnalyzer:
    def __init__(self):
        self._text = ''

    def set_text(self, text):
        self._text = text

    def get_text(self):
        return self._text

    def get_polarity(self):
        try:
            polarity = ''
            tweet = TextBlob(self.get_text()).translate(to = 'en').sentiment
            if tweet.polarity > 0:
                polarity = 'positivo'
            elif tweet.polarity < 0:
                polarity = 'negativo'
            else:
                polarity = 'neutral'

            return polarity
        except:
            return 'neutral'

    def _bag_of_words(self, s, words):
        bag = [0 for _ in range(len(words))]
        s_words = nltk.word_tokenize(s)
        s_words = [stemmer.stem(word.lower()) for word in s_words]

        for se in s_words:
            for i, w in enumerate(words):
                if w == se:
                    bag[i] = 1

        return numpy.array(bag)

    def _get_response(self, tweet):
        text = ''
        results = model.predict([self._bag_of_words(tweet['text'], words)])[0]
        results_index = numpy.argmax(results)
        tag = labels[results_index]
        if results[results_index] > 0.7:
            for tg in data['intents']:
                if tg['tag'] == tag:
                    responses = tg['responses']

            if tag != 'sentimientos':
                text = random.choice(responses)
            else:
                with open('feelings.json') as f:
                    motivation = json.load(f)
                text = random.choice(responses) + ' ' + random.choice(motivation['phrases'])
        else:
            if tweet['polarity'] != 'negativo':
                text = 'La verdad es que no entiendo. Cuentame ¿Cómo estás?'
            else:
                with open('feelings.json') as f:
                    responses = json.load(f)
                text = random.choice(responses['phrases'])
        
        return text
