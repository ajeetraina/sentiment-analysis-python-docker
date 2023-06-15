# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script to the container
COPY sentiment_analysis.py .

# Set the command to run the Python script
CMD [ "python", "sentiment_analysis.py" ]
