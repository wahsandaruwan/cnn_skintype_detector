import os
import uuid

from UseModel import get_skin_type
from PreProcessImage import pre_process_img
from flask import Flask, request, jsonify
from flask_cors import CORS
from json import JSONEncoder
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

# Load environmental variables
load_dotenv()

# App initalization
app = Flask(__name__)
CORS(app)

# Initial POST route
@app.route('/predict', methods=['POST'])
def index():
    # Validate the image file
    if "file" not in request.files:
        return jsonify({"error": "Image not provided"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No image selected"}), 400
    
    # Generate a secure unique file name
    filename = uuid.uuid4().hex+"_"+secure_filename(file.filename)

    # Save the file
    file.save(os.path.join(os.getenv("UP_INIT_DIR"), filename))

    # Pre-process the image
    new_filename = pre_process_img(os.getenv("UP_INIT_DIR")+filename)

    # Get the skin type
    skin_type = get_skin_type(os.getenv("UP_PP_DIR")+new_filename)

    return jsonify({"skin_type": skin_type}), 200

# Execute the app
if __name__ == "__main__":
    app.run(host="0.0.0.0")