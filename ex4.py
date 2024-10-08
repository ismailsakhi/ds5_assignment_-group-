#ex4
import pandas as pd
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Set seed for consistent results
DetectorFactory.seed = 0

# Load the Excel file containing the tweets
file_path = 'tweets.xlsx'  # Ensure the file is in the current directory or provide the full path
df = pd.read_excel(file_path)

# Define a function to detect the language of each tweet
def detect_language(tweet):
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
df.to_excel('tweets_with_languages.xlsx', index=False)  # Save the output to a new Excel file
print(df)


