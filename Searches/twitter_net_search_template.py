# Searches for tweets you are interested in
import tweepy

consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

auth = tweepy.OauthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#what you want to ask
tweets = api.search(q='deep_learning', lang='en', count = 100, tweet_mode='standard')
