import tweepy
import time

consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'

key = 'KEY'
secret = 'SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
