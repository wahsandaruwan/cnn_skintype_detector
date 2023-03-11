import numpy as np

from keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array

model = load_model("./Model/final_model.h5")

img_path = "./TestImages/DRY_0687.JPG"
img = load_img(img_path, target_size=(500,500))

i = img_to_array(img)/255
input_arr = np.array([i])
input_arr.shape

pred = np.argmax(model.predict(input_arr))

if pred == 0:
  print("Dry Skin")
else:
  print("Oily Skin")