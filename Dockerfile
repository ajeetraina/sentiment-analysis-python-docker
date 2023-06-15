FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the Python script to the container
COPY sentiment_analysis.py /app

# Install NLTK
RUN pip install nltk

# Download required NLTK data
RUN python -c "import nltk; nltk.download('vader_lexicon')"

# Run the Python script
CMD [ "python", "sentiment_analysis.py" ]
