from fnmatch import translate
from matplotlib.pyplot import polar
from textblob import TextBlob
from .get_tweet import get_data
from .clean_data import clean_text
from googletrans import Translator
translator = Translator()
def tweet_sentiment(query, num_items, lang):
    
    fetched_tweets = get_data(query, num_items, lang)
    tweet_list = []
    for tweet in fetched_tweets:
        tweet_dict = {}
        text = tweet.text
        text1 = tweet.text
        if translator.detect(text) != 'en':
            translation = translator.translate(text, dest='en')
            text = translation.text
        text_cleaned = clean_text(text)
        blob = TextBlob(text_cleaned)
        tweet_dict['Text'] = text1
        sentiment = blob.sentiment.polarity
        if sentiment < 0:
            polarity = 'Negative'
            tweet_dict['Polarity'] = polarity
        elif sentiment == 0:
            polarity = 'Neutral'
            tweet_dict['Polarity'] = polarity
        else:
            polarity = 'Positive'
            tweet_dict['Polarity'] = polarity
        tweet_list.append(tweet_dict)

    return tweet_list
    


def sentence_sentiment(text):
    sentence_analysis = {}
    if translator.detect(text) != 'en':
            translation = translator.translate(text, dest='en')
            text = translation.text
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment < 0:
           polarity = 'Negative'
    elif sentiment == 0:
        polarity = 'Neutral'
    else:
        polarity = 'Positive'
    sentence_analysis['text'] = text
    sentence_analysis['polarity'] = polarity

    return sentence_analysis

