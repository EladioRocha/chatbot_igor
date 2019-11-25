import json
from TextAnalyzer import TextAnalyzer
from bs4 import BeautifulSoup
import urllib.request

data = urllib.request.urlopen('https://frases.top/frases-motivacion-motivadoras/').read().decode()
soup = BeautifulSoup(data)
tags = soup('li')
phrases = {'phrases': []}

for tag in tags:
    try:
        if int(tag.get_text().split()[0].split('.')[0]):
            sentence = tag.get_text().split()
            del sentence[0]
            phrases['phrases'].append(' '.join(sentence))
    except:
        pass

with open('feelings.json', 'w') as fp:
    json.dump(phrases, fp)