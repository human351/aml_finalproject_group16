# Use the official Python image as a base image
FROM python:3.10-slim

# Use an official TensorFlow runtime as a parent image
FROM tensorflow/tensorflow:2.11.0

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Define environment variable
ENV NAME XRayPneumoniaChecker

# Run app.py when the container launches
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
