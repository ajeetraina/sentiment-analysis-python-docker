# Sentiment Analysis app using Python, NLTK (Natural Language Toolkit), and Docker:

## Clone the repository

```
git clone https://github.com/ajeetraina/sentiment-analysis-python-docker
```

# Install NLTK
RUN pip install nltk

# Download required NLTK data
RUN python -c "import nltk; nltk.download('vader_lexicon')"


```
 docker build -t sentiment-analysis-app .
```


Once the image is built, run the Docker container:

```
docker run -it sentiment-analysis-app
```

Enter the text for sentiment analysis when prompted, and the sentiment label and scores will be displayed.

This sample code sets up a basic Sentiment Analysis app using Python, NLTK, and Docker. It uses NLTK's SentimentIntensityAnalyzer for sentiment analysis and provides a simple command-line interface. You can further enhance the app by integrating it into a web application framework or adding more advanced NLP techniques.
