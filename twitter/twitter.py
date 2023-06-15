import tweepy
from textblob import TextBlob

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Define search parameters
search_query = "Python programming"  # Modify with your desired search query
tweet_count = 100  # Number of tweets to fetch

# Fetch tweets
tweets = tweepy.Cursor(api.search, q=search_query, lang="en").items(tweet_count)

# Perform sentiment analysis on each tweet
for tweet in tweets:
    analysis = TextBlob(tweet.text)
    polarity = analysis.sentiment.polarity

    # Classify sentiment based on polarity
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    # Print tweet text and sentiment
    print(f"Tweet: {tweet.text}")
    print(f"Sentiment: {sentiment}")
    print()

