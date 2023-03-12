import os
import numpy as np

from keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array

# Load model
model = load_model("./Model/final_model.h5")

def get_skin_type(img_path):
  # Load image
  img = load_img(img_path, target_size=(500,500))

  # Create an input using the image
  i = img_to_array(img)/255
  input_arr = np.array([i])
  input_arr.shape

  # Get the prediction
  pred = np.argmax(model.predict(input_arr))

  # Remove preprocessed image file
  os.remove(img_path)

  # Display the output
  if pred == 0:
    return "Dry Skin"
  else:
    return "Oily Skin"