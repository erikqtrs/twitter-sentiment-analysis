import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
def clean_text(text):
    """
        Function to clean each tweet text
    """
    stop_words = list( stopwords.words('english') )
    text = re.sub(r'^RT[\s]+', '', text)
    text = re.sub(r'https?:\/\/.*[\r\n]*', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'@[A-Za-z0-9]+', '', text)
    text = re.sub(r'\n+', '', text)
    text = re.sub(r'\r+', '', text)
    text = re.sub(r':+', '', text)
    text = text.lower()
    text_token = word_tokenize(text)
    clean_words = [w for w in text_token if w not in stop_words]

    # remove punctuation
    unpuctuated_text = [char for char in clean_words if char not in string.punctuation]
    clean_text = ' '.join(unpuctuated_text)
    
    return clean_text