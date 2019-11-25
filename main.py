import time

##### OUR MODULES #####
from TwitterClient import TwitterClient

def main():
    twitterClient = TwitterClient()
    while True:
        tweets = twitterClient.get_tweets_sentiments(twitterClient.get_tweets())
        twitterClient.retweet(tweets)
        time.sleep(30)

if __name__ == "__main__":
    main()