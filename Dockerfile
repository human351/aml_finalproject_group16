# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run"]
