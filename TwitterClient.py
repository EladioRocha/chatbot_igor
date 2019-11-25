import re, time, tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
from TextAnalyzer import TextAnalyzer

##### OUR MODULES #####
import settings

class TwitterClient:

    def __init__(self):
        self._textAnalyzer = TextAnalyzer()
        self._retweeted = {'1'}
        try:
            self._auth = OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
            self._auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)
            self._api = tweepy.API(self._auth)            
        except:
            print('Error: Fallo al intentar autenticarse')

    def get_tweets(self):
        tweets = []
        for mentions in tweepy.Cursor(self._api.mentions_timeline).items():
            tweets.append({'id': mentions.id, 'text': self.clean_tweet(mentions.text), 'author': mentions.author.screen_name, 'polarity': ''})

        return tweets
 
    def clean_tweet(self, tweet):
        return tweet.replace(re.compile(r'^@[A-Za-z0-9]+[\s]').search(tweet).group(), '')

    def get_tweets_sentiments(self, tweets):
        for tweet in tweets:
            self._textAnalyzer.set_text(tweet['text'])
            tweet['polarity'] = self._textAnalyzer.get_polarity()

        return tweets

    def retweet(self, tweets):
        for tweet in tweets:
            try:
                print(self._retweeted)
                if not str(tweet['id']) in self._retweeted:
                    self._api.update_status('@{} {}'.format(tweet['author'], self._textAnalyzer._get_response(tweet)), tweet['id']) # TwitterId
                    self._retweeted.add(str(tweet['id']))    
            except:
                print('Ya ha sido respondido')
