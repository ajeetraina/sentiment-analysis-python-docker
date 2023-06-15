# In this example, the code reads the Twitter data from a JSON file called twitter_data.json. 
# Each tweet in the JSON file is processed individually, and the sentiment analysis is performed using TextBlob. 
# The sentiment polarity is calculated, and based on its value, a sentiment label (Positive, Negative, or Neutral) is assigned. 
# The tweet text and sentiment label are then printed.

Make sure to replace 'twitter_data.json' with the actual path to your JSON file containing the Twitter data.

By storing the Twitter data in a JSON file, you can easily process large amounts of data and perform sentiment analysis on each tweet. This approach allows you to decouple the data storage from the sentiment analysis code and provides flexibility in handling different data sources.

import json
from textblob import TextBlob

# Load the JSON data from a file
with open('twitter_data.json', 'r') as file:
    data = json.load(file)

# Process each tweet in the JSON data
for tweet in data['tweets']:
    text = tweet['text']

    # Perform sentiment analysis using TextBlob
    analysis = TextBlob(text)
    sentiment = analysis.sentiment.polarity

    # Determine the sentiment label
    if sentiment > 0:
        label = 'Positive'
    elif sentiment < 0:
        label = 'Negative'
    else:
        label = 'Neutral'

    # Print the tweet text and sentiment label
    print(f'Tweet: {text}')
    print(f'Sentiment: {label}')
    print('---')
