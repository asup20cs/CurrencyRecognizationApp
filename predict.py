import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load the pre-trained model
model = load_model('updated_indian.h5')

# Define a function to load, preprocess, and predict for an image
def predict_image(image_path, target_size=(64, 64)):
  """
  Loads an image, preprocesses it, and predicts the class using the model.

  Args:
      image_path (str): Path to the image file.
      target_size (tuple, optional): Target size for resizing the image. Defaults to (64, 64).

  Returns:
      str: Predicted currency name or "Unknown" if prediction confidence is low.
  """
  # Load the image
  try:
    img = load_img(image_path, target_size=target_size)
  except FileNotFoundError:
    print(f"Error: Image file not found at {image_path}")
    return "Unknown"

  # Preprocess the image
  img_array = img_to_array(img)
  img_array = np.expand_dims(img_array, axis=0)

  # Make prediction using the model
  predictions = model.predict(img_array)
  predicted_class = np.argmax(predictions)

  # Confidence threshold (adjust based on your model's performance)
  confidence_threshold = 0.8

  # Check prediction confidence before assigning currency
  if predictions[0][predicted_class] >= confidence_threshold:
    predicted_currency = currency_map.get(predicted_class)
  else:
    predicted_currency = "Unknown"

  return predicted_currency

# Indian currency map (modify class indices based on your model's output)
currency_map = {
    0: "10 Rupees",
    1: "100 Rupees",
    2: "20 Rupees",
    3: "200 Rupees",
    4: "2000 Rupees",
    5: "50 Rupees",
    6: "500 Rupees"
}

# Get the image path (replace with your actual path)
image_path = '/content/100.jpeg'

# Predict the currency for the image
predicted_currency = predict_image(image_path)

# Print the predicted currency
print(f"Predicted Currency: {predicted_currency}")
