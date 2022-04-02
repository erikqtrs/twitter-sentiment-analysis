import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

class ConnectApi:
    def __init__(self):
            self.CONSUMER_KEY = os.getenv('CONSUMER_KEY')
            self.CONSUMER_KEY_SECRET = os.getenv('CONSUMER_KEY_SECRET')
            self.ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
            self.ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

    def authentication_api(self):
        self.auth = tweepy.OAuthHandler(
            self.CONSUMER_KEY, self.CONSUMER_KEY_SECRET
        )

        self.auth.set_access_token(
            self.ACCESS_TOKEN, self.ACCESS_TOKEN_SECRET
        )
    
    def connection_api(self):
        self.authentication_api()
        self.api = tweepy.API(self.auth)
        return self.api
