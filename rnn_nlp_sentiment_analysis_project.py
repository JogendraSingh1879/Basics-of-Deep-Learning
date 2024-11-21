# -*- coding: utf-8 -*-
"""RNN-NLP-Sentiment Analysis PROJECT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hL-9SDezsBEr2XlU6Q-TRznGfP3_MmfZ
"""

# Importing the Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

#step 1 Load the IMDB Dataset
vocab_size = 10000
max_len = 200
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words = vocab_size)

#step 2 Preprocessing
x_train = pad_sequences(x_train, maxlen = max_len)
x_test = pad_sequences(x_test, maxlen = max_len)

# Step 3: Build the RNN model
model = Sequential([
    Embedding(input_dim = vocab_size, output_dim = 32, input_length = max_len),
    SimpleRNN(units = 32),
    Dense(units = 1, activation = 'sigmoid')
])

# Compile the model
model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Summary
model.summary()

#Step 4: Training the model
history = model.fit(x_train, y_train, batch_size = 64, epochs = 15,
                    validation_data=(x_test, y_test))

#Step 5 evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)

print(f"Test Accuracy:{test_acc}")

#Step 6: Prediction
sample_review ="This movies was fantastic! I really enjoyed it."
from tensorflow.keras.preprocessing.text import Tokenizer
tokenizer = imdb.get_word_index()

#tokenize the input text
sample_review_tokens = [tokenizer.get(word,0) for word in sample_review.lower().split()]
sample_review_tokens_padded = pad_sequences([sample_review_tokens], maxlen = max_len)

#make prediction

predicted = model.predict([sample_review_tokens_padded])
print(f"Predicted Sentiment: {'Positive' if predicted > 0.5 else 'Negative'}")