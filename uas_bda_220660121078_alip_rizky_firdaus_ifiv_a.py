# -*- coding: utf-8 -*-
"""UAS_BDA_220660121078_ALIP-RIZKY-FIRDAUS_IFIV-A.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UD6FiFay9SnvSd_dQ6-oIed7hKYM6mgg
"""

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
import matplotlib.pyplot as plt
from tabulate import tabulate

# Membaca data dari file yang diunggah
data = pd.read_csv('Reddit_Data.csv')

# Menggantikan np.nan dengan string kosong ''
data['clean_comment'].fillna('', inplace=True)

# Mengambil hanya kolom 'clean_comment'
comments = data['clean_comment'].values

# Menggunakan TF-IDF untuk mengubah teks menjadi representasi numerik
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(comments).toarray()

# Membagi data menjadi data latih dan data uji
X_train, X_test, comments_train, comments_test = train_test_split(X, comments, test_size=0.2, random_state=42)

# Membuat model Autoencoder
input_dim = X_train.shape[1]
encoding_dim = 32

input_layer = Input(shape=(input_dim,))
encoder = Dense(encoding_dim, activation="relu")(input_layer)
decoder = Dense(input_dim, activation="sigmoid")(encoder)

autoencoder = Model(inputs=input_layer, outputs=decoder)
autoencoder.compile(optimizer='adam', loss='mse')

# Melatih model Autoencoder
history = autoencoder.fit(X_train, X_train, epochs=20, batch_size=256, validation_split=0.2, verbose=1)

# Menggunakan model untuk mendeteksi anomali
X_train_pred = autoencoder.predict(X_train)
mse = np.mean(np.power(X_train - X_train_pred, 2), axis=1)
threshold = np.percentile(mse, 95)  # Menentukan threshold dari data latih

X_test_pred = autoencoder.predict(X_test)
mse_test = np.mean(np.power(X_test - X_test_pred, 2), axis=1)

# Menandai anomali berdasarkan threshold
anomalies = mse_test > threshold

# Tampilkan jumlah anomali terdeteksi dengan format yang menonjol
print(f'\n===============================================')
print(f' Jumlah anomali terdeteksi: {np.sum(anomalies)} ')
print(f'===============================================\n')

# Menampilkan komentar anomali dalam tabel menggunakan tabulate
anomalous_comments = comments_test[anomalies]
anomalous_comments_table = pd.DataFrame(anomalous_comments[:10], columns=['Anomalous Comments'])

# Menggunakan tabulate untuk tampilan tabel yang lebih baik
table = tabulate(anomalous_comments_table, headers='keys', tablefmt='pretty', showindex=False)
print(table)