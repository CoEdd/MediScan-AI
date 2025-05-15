import os
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import cv2

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model', 'pneumonia_cnn.h5')

def predict_image(image_path):
    # Load model when needed
    model = load_model(MODEL_PATH)
    # Read the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    img = img.reshape(1, 224, 224, 1)
    pred = model.predict(img)[0][0]
    return "Pneumonia" if pred > 0.5 else "Normal"