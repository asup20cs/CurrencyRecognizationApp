import os
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Define the list of folder paths (only two directories)
folder_paths = ["images_test/indian"]

# Initialize an empty list to store image paths
image_paths = []

# Loop through each folder
for folder_path in folder_paths:
    # Ensure the folder exists
    if not os.path.isdir(folder_path):
        print(f"Warning: Folder not found: {folder_path}")
        continue

    # Get a list of image files in the current folder
    image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path)
                                 if os.path.isfile(os.path.join(folder_path, f))]

    # Add all image paths from this folder
    image_paths.extend(image_files)

# Print the total number of selected images
print(f"Total image paths: {len(image_paths)}")

# Replace with your image path and labels


model=load_model("models/indian.h5")
labels = ["10", "100", "20", "200", "2000", "50","500"]
# Replace with your image path and labels
def predict_indian(image_path):

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
for i in range(len(image_paths):
    print(image_paths[i])
    predict_indian(image_paths[i])