import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load model and tokenizer
model = tf.keras.models.load_model("C:/Users/2005g/OneDrive/Desktop/AI/toxic/toxic_comment_model.h5")

with open("C:/Users/2005g/OneDrive/Desktop/AI/toxic/tokenizer.pkl", "rb") as handle:
    tokenizer = pickle.load(handle)

# Test comments
test_comments = ["You are amazing", "I hate you", "This is horrible"]

def predict_comment(comment):
    seq = tokenizer.texts_to_sequences([comment])

    print(f"Comment: {comment}")
    print(f"Tokenized: {seq}")  # Debugging tokenized output

    padded = pad_sequences(seq, maxlen=150, padding="post", truncating="post")

    print(f"Padded Sequence: {padded}")  # Debugging padded output

    raw_score = model.predict(padded)[0][0]
    return round(raw_score * 100, 2)

for comment in test_comments:
    print(f"Comment: {comment} -> Toxicity Score: {predict_comment(comment)}")
