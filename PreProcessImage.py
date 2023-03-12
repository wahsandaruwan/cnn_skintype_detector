import os
import cv2
import uuid
import numpy as np

def pre_process_img(img_path):
    # Read image
    img = cv2.imread(img_path)

    # Select the left cheek region manually
    left_cheek = (80, 100)

    # Crop image
    cropped = img[left_cheek[1]:, :left_cheek[0]]

    # Resize image
    resized_image = cv2.resize(cropped, (500, 500))

    # Reduce the brightness of image
    reduce_br_img = cv2.convertScaleAbs(resized_image, alpha=0.75, beta=0)

    # Reduce illumination of image
    reduce_ill_img = cv2.cvtColor(reduce_br_img, cv2.COLOR_BGR2RGB)

    # Save image
    new_filename = uuid.uuid4().hex+"_final.jpg"
    cv2.imwrite(os.getenv("UP_PP_DIR")+new_filename, reduce_ill_img)

    return new_filename