import os
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model', 'pneumonia_cnn.h5')
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os

# Load model once
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model', 'pneumonia_cnn.h5')
model = load_model(MODEL_PATH)

def predict_image(image_path):
    # Read the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Resize the image to match the input shape of the modelPython: Configure Language Specific Settings
    img = cv2.resize(img, (224, 224))
    # Normalize the image data
    img = img / 255.0
    # Reshape the image to add batch dimension
    img = img.reshape(1, 224, 224, 1)
    
    # Predict using the model
    pred = model.predict(img)[0][0]
    
    # Return prediction
    return "Pneumonia" if pred > 0.5 else "Normal"
