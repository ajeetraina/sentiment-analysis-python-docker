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
