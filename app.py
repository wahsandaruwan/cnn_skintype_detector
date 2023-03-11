import os

from UseModel import get_skin_type
from flask import Flask, request, jsonify
from flask_cors import CORS
from json import JSONEncoder

# App initalization
app = Flask(__name__)
CORS(app)

# Upload folder
app.config["UPLOAD_FOLDER"] = "./Uploads"

# Initial GET route
@app.route('/predict', methods=['POST'])
def index():
    # Validate the image file
    if "file" not in request.files:
        return jsonify({"error": "Image not provided"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No image selected"}), 400
    # Save the file
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))

    # Get the skin type
    skin_type = get_skin_type("./Uploads/"+file.filename)

    return jsonify({"skin_type": skin_type}), 200

# Execute the app
if __name__ == "__main__":
    app.run(host="0.0.0.0")