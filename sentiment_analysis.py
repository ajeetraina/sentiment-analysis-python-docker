# Import necessary libraries
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function to perform sentiment analysis
def perform_sentiment_analysis(text):
    # Analyze sentiment using NLTK's SentimentIntensityAnalyzer
    sentiment_scores = sia.polarity_scores(text)

    # Determine sentiment label based on compound score
    if sentiment_scores['compound'] >= 0.05:
        sentiment_label = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'

    return sentiment_label, sentiment_scores

# Main function
def main():
    # Get input text from the user
    input_text = input("Enter text for sentiment analysis: ")

    # Perform sentiment analysis
    sentiment_label, sentiment_scores = perform_sentiment_analysis(input_text)

    # Print the sentiment label and scores
    print("Sentiment Label:", sentiment_label)
    print("Sentiment Scores:", sentiment_scores)

# Execute the main function
if __name__ == '__main__':
    main()
