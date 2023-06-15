# Sentiment Analysis app using Python, NLTK (Natural Language Toolkit), and Docker:

## Clone the repository

```
git clone https://github.com/ajeetraina/sentiment-analysis-python-docker
```

# Building Docker Image



```
 docker build -t sentiment-analysis-app .
```


## Runing the Docker container

```
docker run -it sentiment-analysis-app
```

```
Enter text for sentiment analysis: I love this product! It exceeded my expectations
Sentiment Label: Positive
Sentiment Scores: {'neg': 0.0, 'neu': 0.572, 'pos': 0.428, 'compound': 0.6696}

```

Enter the text for sentiment analysis when prompted, and the sentiment label and scores will be displayed.

This sample code sets up a basic Sentiment Analysis app using Python, NLTK, and Docker. It uses NLTK's SentimentIntensityAnalyzer for sentiment analysis and provides a simple command-line interface. You can further enhance the app by integrating it into a web application framework or adding more advanced NLP techniques.
