import numpy as np
import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model("C:/Users/2005g/OneDrive/Desktop/AI/toxic/toxic_comment_model.h5")

# Load the tokenizer
with open("C:/Users/2005g/OneDrive/Desktop/AI/toxic/tokenizer.pkl", "rb") as handle:
    tokenizer = pickle.load(handle)

# Function to predict toxicity score
def predict_toxicity(comment):
    seq = tokenizer.texts_to_sequences([comment])
    padded = pad_sequences(seq, maxlen=150)  # Ensure same length as training
    score = model.predict(padded)[0][0]  # Sigmoid output

    print(f"Raw Model Score: {score}")  # Debugging line to check actual output

    # Convert score to percentage
    return round(score * 100, 2)

# Sample test cases
test_comments = [
    "You are such an idiot, this is the worst thing I've ever seen!",  # Clearly toxic
    "Thank you for sharing, this is very helpful!",  # Clearly non-toxic
    "Shut up! You're so dumb.",  #incl
    "I totally disagree with your opinion, but I respect it.",  # Non-toxic
]

for comment in test_comments:
    print(f"Comment: {comment}")
    print(f"Toxicity Score: {predict_toxicity(comment)}%")
    print("-" * 50)
