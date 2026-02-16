# ================================
# IMDB Sentiment Analysis App
# ================================

import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
import streamlit as st

# -------------------------------
# Parameters (MUST match training)
# -------------------------------
max_features = 10000   # vocab size
max_length = 500       # sequence length

# -------------------------------
# Load word index + reverse index
# -------------------------------
word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}

# -------------------------------
# Load trained model
# -------------------------------
model = load_model('Simple_RNN_Imdb.h5')

# -------------------------------
# Preprocess function (FIXED)
# -------------------------------
import re

def preprocess_text(text):
    # normalize apostrophes
    text = text.lower()
    text = re.sub(r"[^\w\s']", "", text)  # remove punctuation

    words = text.split()

    encoded_review = []
    for word in words:
        index = word_index.get(word, 2)
        if index < max_features:
            encoded_review.append(index + 3)
        else:
            encoded_review.append(2)

    padded_review = sequence.pad_sequences([encoded_review], maxlen=max_length)
    return padded_review


# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="IMDB Sentiment Analyzer", page_icon="🎬")

st.title("🎬 IMDB Movie Review Sentiment Analysis")
st.write("Enter a movie review to classify sentiment using a Simple RNN model.")

user_input = st.text_area("✍️ Movie Review")

if st.button("🔍 Classify Sentiment"):

    if user_input.strip() == "":
        st.warning("⚠️ Please enter a review before clicking classify.")

    else:
        preprocessed_input = preprocess_text(user_input)

        prediction = model.predict(preprocessed_input)
        score = prediction[0][0]

        sentiment = "✅ Positive" if score > 0.5 else "❌ Negative"

        st.subheader("Result")
        st.write(f"**Sentiment:** {sentiment}")
        st.write(f"**Confidence Score:** {score:.4f}")

        # confidence bar
        st.progress(float(score))

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Built with ❤️ using TensorFlow & Streamlit")
