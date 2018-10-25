# importing the module 
import tweepy 

# personal details 
consumer_key ="krklOEjpcPNJTFVf553xehNhi"
consumer_secret ="qZtbTKGDYBwJ8yI0AuRvOlVyQa1e11g2RvjdRmQsc2LzLN7wlX"
access_token ="1055369228130217984-AsL0Yu07HvGWStYKMqbY5LzXK1T6Fo"
access_token_secret ="y9Opz9fVQ0YgDxxCxpwSn2ryvSYV8w7QsmwBtkSkq0EIF"

# authentication of consumer key and secret 
auth = tweepy.OAuthHandler(consumer_key,consumer_secret) 

# authentication of access token and secret 
auth.set_access_token(access_token,access_token_secret) 
api = tweepy.API(auth) 

# update the status 
sta=str(input("Status msg:"))
api.update_status(status=sta) 
