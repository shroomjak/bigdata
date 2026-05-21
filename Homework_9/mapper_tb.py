import sys
import numpy as np
import keras
import tb

VOCAB_PATH = 'imdb_lstm.voc.npy'
WEIGHTS_PATH = 'imdb_lstm.weights.h5'

vocab = np.load(VOCAB_PATH, allow_pickle=True)

encoder = keras.layers.TextVectorization(
    name='tv',
    max_tokens=1000,
    vocabulary=vocab
)

model = keras.Sequential([
    encoder,
    keras.layers.Embedding(input_dim=len(vocab), output_dim=16,
                           mask_zero=True),
    keras.layers.LSTM(16),
    keras.layers.Dense(1, activation='sigmoid')
])

model.build(input_shape=(None,))
model.load_weights(WEIGHTS_PATH)

while True:
    data = tb.read(3)  # id, article, highlights
    if data is None:
        break

    rec_id, article, highlights = data

    if not rec_id or not article:
        continue

    try:
        pred = model.predict(
            np.array([article], dtype=object),
            verbose=0
        )[0][0]
        rating = float(pred) * 9.0 + 1.0

        print(f"{rec_id}\t{pred:.6f}\t{rating:.2f}")
    except Exception as e:
        sys.stderr.write(f"Error {rec_id}: {e}\n")