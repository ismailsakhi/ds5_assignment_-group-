#ex4.1
import pandas as pd
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Set seed for consistent results
DetectorFactory.seed = 0

# Load the Excel file containing the tweets
df = pd.read_excel('tweets.xlsx' )

# Define a function to detect the language of each tweet
def detect_language(tweet):
    """
    detecting the language of the messages 
    input:
        table with the messages
    output:
        column with the detected languges
    """
    try:
        # Detect the language of the tweet
        return detect(tweet)
    except LangDetectException:
        # If detection fails, return 'Unknown'
        return 'Unknown'
    except Exception as e:
        # Catch any other unexpected exceptions
        return 'Unknown'

# Apply the language detection function to the 'Tweet' column
df['language'] = df['Tweet'].apply(detect_language)

# Save the results back to an Excel file or display it
df.to_excel('ex4.1_languages_detection.xlsx', index=False)  # Save the output to a new Excel file

#In the provided exel file there are a lot of messegas cosisting of the so-called Unicode 
#for example some messages supposed to be in russian, however they were trascripted in "ÐŸÐ¾ÐµÑ…Ð°Ð»Ð° Ð½Ð° ÐºÐ°Ñ‚Ð¾Ðº"
#which is not russian for sure (i'm a native speaker, so you can trust me). 
#unfortunately,I've no idea how to fix it and it leads to some errors in language detection 

#ex4.2

from textblob import TextBlob
from nltk.sentiment import SentimentIntensityAnalyzer
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Function to analyze sentiment for English tweets using TextBlob
def analyze_sentiment_english(tweet):
    blob = TextBlob(str(tweet))  # Ensure tweet is converted to string
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'

# Function to analyze sentiment for non-English tweets using NLTK's SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

def analyze_sentiment_other(tweet):
    scores = sia.polarity_scores(str(tweet))  # Ensure tweet is converted to string
    compound = scores['compound']
    if compound >= 0.05:
        return 'positive'
    elif compound <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Function to analyze sentiment based on language
def analyze_sentiment(tweet, language):
    if language == 'en':
        return analyze_sentiment_english(tweet)
    else:
        return analyze_sentiment_other(tweet)

# Apply sentiment analysis based on language
df['sentiment'] = df.apply(lambda row: analyze_sentiment(row['Tweet'], row['language']), axis=1)

# Save the results to a new Excel file
df.to_excel('ex4.2_sentiment_detection.xlsx', index=False)

