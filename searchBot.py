import tweepy
import time

consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'

key = 'KEY'
secret = 'SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

# Buscar en twitter el siguiente hashtag y retuitear los X más recientes que lo tengan

hashtag = '#HASHTAG'
tweetNumber = 10

tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)


def searchBot():
    for tweet in tweets:
        try:
            tweet.retweet()
            print("Retweet done!")
            time.sleep(3)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(3)


searchBot()

# SACAR LOS ÚLTIMOS TWEETS DE UNA CUENTA

# user = 'USER'
# tweetNumber = 10

# tweets = tweepy.Cursor(api.search, user).items(tweetNumber)

# def searchBot():
#     for tweet in tweets:
#         try:
#             print(tweet.text)
#             time.sleep(5)
#         except tweepy.TweepError as e:
#             print(e.reason)
#             time.sleep(5)

# searchBot()
