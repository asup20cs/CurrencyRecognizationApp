import cv2
import time
from PIL import Image  # For image conversion (optional)
import tkinter as tk  # For displaying camera feed
import numpy as np

# Function to capture image and display real-time feed
def capture_image(filename="captured_image.jpg"):
  # Initialize camera
  cap = cv2.VideoCapture(0)

  # Create a window to display camera feed
  window_name = "Currency Detection Camera"
  cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

  # Wait for camera to warm up
  time.sleep(2)

  while True:
    # Capture frame from camera
    ret, frame = cap.read()

    # Optionally convert to RGB (if needed for your model)
    if frame is not None:
      rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
      image = Image.fromarray(rgb_frame) # Create PIL Image object (optional)
      

    # Display camera feed in the window
    cv2.imshow(window_name, frame)

    # Capture image on key press (optional)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):  # Capture on 'c' key press (replace with desired key)
      if image is not None:
        image.save(filename)
        print(f"Image captured and saved as: {filename}")
      break

    # Exit on 'q' key press
    if key == ord('q'):
      break

  # Release camera resources
  cap.release()
  cv2.destroyAllWindows()

# Example usage (replace with integration logic in app.py)
def start_camera_capture():
    capture_image()