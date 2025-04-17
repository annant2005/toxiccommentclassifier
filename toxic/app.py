from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import numpy as np

# Load Model & Tokenizer
model = tf.keras.models.load_model("C:/Users/2005g/OneDrive/Desktop/AI/toxic/toxic_comment_model.h5")

with open("C:/Users/2005g/OneDrive/Desktop/AI/toxic/tokenizer.pkl", "rb") as handle:
    tokenizer = pickle.load(handle)

# Constants
MAX_LEN = 150

# Initialize Flask App
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get comment from user
    comment = request.form.get("comment")
    
    # Tokenize & Pad
    seq = tokenizer.texts_to_sequences([comment])
    padded = pad_sequences(seq, maxlen=MAX_LEN, padding="post", truncating="post")

    # Predict Toxicity Score
    raw_score = model.predict(padded)[0][0]  # Probability (0 to 1)
    toxicity_score = round(raw_score * 100, 2)  # Convert to %

    return render_template("index.html", comment=comment, toxicity_score=toxicity_score)

if __name__ == "__main__":
    app.run(debug=True)
