import sys
import numpy as np
import keras
import tb

VOCAB_PATH = 'negpos_lstm.voc.npy'
WEIGHTS_PATH = 'negpos_lstm.weights.h5'
VOCAB_SIZE = 5000

vocab = np.load(VOCAB_PATH, allow_pickle=True)

encoder = keras.layers.TextVectorization(
    name='tv',
    max_tokens=VOCAB_SIZE,
    vocabulary=vocab
)

model = keras.Sequential([
    encoder,
    keras.layers.Embedding(input_dim=len(vocab), output_dim=16, mask_zero=True),
    keras.layers.Bidirectional(keras.layers.LSTM(16)),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

model.build(input_shape=(None,))
model.load_weights(WEIGHTS_PATH)

for _ in range(100):
    data = tb.read(2)  # id, comment
    if data is None:
        break

    label, comment = data

    if not label or not comment:
        continue

    try:
        pred = model.predict(
            np.array([comment], dtype=object),
            verbose=0
        )[0][0]

        print(f"{label}\t{comment}\tpredict: {pred:.2f}")
    except Exception as e:
        sys.stderr.write(f"Error {label}: {e}\n")