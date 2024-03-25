from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Load the model
model_path = "updatedmodel.h5"
model = load_model(model_path)

# Replace with your image path and labels
def predict_image(image_path):
    labels = ["10", "100", "20", "200", "2000", "50", "500"]

# Preprocess the image
    img = Image.open(image_path)
    img = img.resize((240, 240))  # Adjust size based on your model
    x = np.array(img)
    x = x / 255.0
    x = np.expand_dims(x, axis=0)

# Make prediction
    prediction = model.predict(x)

# Interpret the prediction
    predicted_class_index = np.argmax(prediction[0])
    predicted_currency = labels[predicted_class_index]
    print(f"Predicted Currency: {predicted_currency}")
    return predicted_currency
