from crypt import methods
from flask import Flask, render_template, request
import sys
import logging
from nlp.sentiment_analysis import tweet_sentiment, sentence_sentiment
app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_tweet', methods= ['POST'])
def predict_tweet():
    if request.method == 'POST':
        
        query = request.form.get('query')
        count = int(request.form.get('items'))
        lang = request.form.get('lang')
        tweets = tweet_sentiment(query, count, lang)
        polarity_tweet = []
        polarity_count = {}
        for tweet in tweets:
            polarity_tweet.append(tweet['Polarity'])
        
        for polarity in polarity_tweet:
            if polarity in polarity_count:
                polarity_count[polarity] += 1
            else:
                polarity_count[polarity] = 1
            
        return render_template('tweets.html', 
            tweets=tweets,
            polarity_count=polarity_count
        )

@app.route('/predict_sentence', methods=['POST'])
def predict_sentence():
    if request.method == 'POST':
        sentence = request.form.get('sentence')
        analysis = sentence_sentiment(sentence)
        return render_template('sentence.html', analysis=analysis)

if __name__ == '__main__':
    app.run(debug= True)