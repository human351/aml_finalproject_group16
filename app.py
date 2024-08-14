from flask import Flask, request, render_template, jsonify, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained model
model = load_model('my_model.h5')

# Class labels
class_labels = {0: 'NORMAL', 1: 'Bacterial Pneumonia', 2: 'Virus Pneumonia'}

def load_and_preprocess_image(img_path, target_size=(299, 299)):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Create a batch of size 1
    img_array /= 255.0  # Rescale pixel values to [0, 1]
    return img_array

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        # Save the file
        file_path = os.path.join('uploads', file.filename)
        file.save(file_path)

        # Make prediction
        img_array = load_and_preprocess_image(file_path)
        predictions = model.predict(img_array)
        
        # Get predicted class and confidence
        predicted_class = np.argmax(predictions, axis=1)[0]
        predicted_label = class_labels[predicted_class]
        confidence_score = np.max(predictions) * 100  # Convert to percentage

        # Generate a response based on confidence and prediction class
        if confidence_score >= 90:
            if confidence_score > 95:
                if predicted_class == 0:  # NORMAL
                    message = f'Your result is NORMAL with a high confidence of {confidence_score:.2f}%. This is reassuring, but we still recommend consulting with a medical professional for a thorough assessment.'
                else:  # Pneumonia cases
                    message = f'Your result is {predicted_label} with a high confidence of {confidence_score:.2f}%. This is significant, and we strongly recommend consulting a healthcare professional for a detailed evaluation.'
            else:
                if predicted_class == 0:  # NORMAL
                    message = f'Your result is NORMAL with a confidence of {confidence_score:.2f}%. It\'s advisable to consult a specialist to get a detailed evaluation.'
                else:  # Pneumonia cases
                    message = f'Your result is {predicted_label} with a confidence of {confidence_score:.2f}%. Please consult a specialist for further evaluation and guidance.'
        else:
            # General message if confidence is below 90%
            message = f'We cannot provide a definitive analysis with confidence below 90%. It is recommended to consult with a specialist for further evaluation.'

        # Send the prediction result, image path, and message
        response = {
            'image_url': f'/uploads/{file.filename}',
            'message': message
        }

        # Only include prediction and confidence details if confidence is 90% or above
        if confidence_score >= 90:
            response.update({
                'prediction': predicted_label,
                'confidence': round(confidence_score, 2)
            })

        return jsonify(response)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

# Ensure the 'uploads' directory exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')
