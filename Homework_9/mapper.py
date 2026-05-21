#!/usr/bin/env python3
import sys
import csv
import numpy as np
import keras

VOCAB_PATH = 'imdb_lstm.voc.npy'
WEIGHTS_PATH = 'imdb_lstm_weights.h5'

# Загрузка словаря
vocab = np.load(VOCAB_PATH, allow_pickle=True)

# Восстановление архитектуры вручную
encoder = keras.layers.TextVectorization(
    name='tv',
    max_tokens=1000,
    vocabulary=vocab
)

model = keras.Sequential([
    encoder,
    keras.layers.Embedding(
        input_dim=len(vocab),
        output_dim=16,
        mask_zero=True
    ),
    keras.layers.LSTM(16),
    keras.layers.Dense(1, activation='sigmoid')
])

# Построение модели
model.build(input_shape=(None,))

# Загрузка весов
model.load_weights(WEIGHTS_PATH)

# Обработка CSV
reader = csv.DictReader(sys.stdin)

for row in reader:
    text = row.get('article', '')
    rec_id = row.get('id', '')

    if not rec_id or not text:
        continue

    try:
        pred = model.predict(
            np.array([text], dtype=object),
            verbose=0
        )[0][0]
        rating = float(pred) * 9.0 + 1.0
        print(f"{rec_id}\t{pred:.6f}\t{rating:.2f}")
    except Exception as e:
        sys.stderr.write(f"Error: {rec_id}: {e}\n")