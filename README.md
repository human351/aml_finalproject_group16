# X-Ray Pneumonia Checker

## Overview

The X-Ray Pneumonia Checker is a sophisticated web application developed to analyze X-ray images and classify them into three categories: NORMAL, Bacterial Pneumonia, or Virus Pneumonia. Utilizing a pre-trained machine learning model, the application provides users with accurate predictions and confidence scores based on the uploaded X-ray images.

## Features

- **Image Upload**: Users can upload X-ray images for analysis.
- **Classification Results**: Predictions categorized as NORMAL, Bacterial Pneumonia, or Virus Pneumonia.
- **Confidence Scores**: Display of confidence levels for predictions.
- **User-Friendly Interface**: Intuitive web interface for easy interaction.

## Getting Started

### Prerequisites

- **Python 3.10**
- **TensorFlow 2.11.0**
- **Flask**

### Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   Ensure you have a `requirements.txt` file with the following contents:

   ```text
   Flask
   tensorflow==2.11.0
   numpy
   ```

   Install the dependencies using:

   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare the Model**

   Place the `my_model.h5` file in the project directory.

5. **Run the Application**

   ```bash
   python app.py
   ```

   The application will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### Docker Setup

To run the application using Docker:

1. **Build the Docker Image**

   ```bash
   docker build -t xray-pneumonia-checker .
   ```

2. **Run the Docker Container**

   ```bash
   docker run -p 8080:8080 xray-pneumonia-checker
   ```

   Access the application at [http://localhost:8080/](http://localhost:8080/).

## File Structure

- **`app.py`**: The main file containing the Flask application code.
- **`my_model.h5`**: The pre-trained TensorFlow model file.
- **`requirements.txt`**: A file listing Python dependencies.
- **`Dockerfile`**: Docker instructions for containerizing the application.
- **`index.html`**: HTML file for the web interface.
- **`uploads/`**: Directory where uploaded images are temporarily stored.

## How to Use

1. Open the application in your web browser.
2. Use the file input field to select and upload an X-ray image.
3. Click "Upload X-Ray" to submit the image.
4. Review the prediction and confidence score displayed on the results page.

## Support and Troubleshooting

- **Error Handling**: Check console logs for error messages if the application is not functioning as expected.
- **File Availability**: Ensure all necessary files, including `my_model.h5`, are present in the project directory.

## Acknowledgments

We acknowledge the contributions of the open-source community and the tools that have facilitated the development of this project.

```

This version integrates all key information into a clear and structured document, ensuring users can easily set up and use the application while providing professional and concise documentation.
