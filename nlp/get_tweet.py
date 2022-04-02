import tweepy
from nlp.twitter_api import ConnectApi

def get_data(query, num_tweets, lang):
    """
        get_data permit obtain the tweets that the user wants\n
        Parameters:
        query: word or phare that can be in the tweet
        num_tweets: indicates the number of tweet
    """
    connection = ConnectApi()
    api = connection.connection_api()
    fetched_tweets = tweepy.Cursor(api.search_tweets,
        q= query, 
        lang= lang
    ).items(num_tweets)

    return fetched_tweets
