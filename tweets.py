import tweepy
from bs4 import BeautifulSoup
from textblob import TextBlob
import io
from decouple import config

consumer_key = config('consumer_key')
consumer_secret = config('consumer_secret')
access_token = config('access_token')
access_token_secret = config('access_token_secret')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='sapanasubedi5', count=211)
lis = []
for tweet in tweets:
    content = tweet.text
    lis.append(content)
    listToStr = ' '.join(map(str, lis))
print(listToStr)

fp = io.open("my_tweets.txt", "w", encoding="utf-8")
fp.writelines(listToStr)







