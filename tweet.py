import tweepy
import tokens  
consumer_key=tokens.consumer_key()
consumer_secret=tokens.consumer_secret()
access_token=tokens.access_token()
access_token_secret=tokens.access_token_secret()
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)  
auth.set_access_token(access_token,access_token_secret) 
api = tweepy.API(auth)  
sta=str(input("Status msg:"))
api.update_status(status=sta) 
