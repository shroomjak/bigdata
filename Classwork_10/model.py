import keras
import numpy as np
import pandas as pd

neg = pd.read_csv('negative.csv', header=None, sep=';').dropna()
neg = neg.iloc[:, [3, 4]]
res1 = neg.rename(columns={3: 'comm', 4: 'val'})
pos = pd.read_csv('positive.csv', header=None, sep=';').dropna()
pos = pos.iloc[:, [3, 4]]
res2 = pos.rename(columns={3: 'comm', 4: 'val'})
res = pd.concat([res1, res2]).reset_index()

x = res['comm'].to_numpy()
y = res['val'].to_numpy()
samples = 200_000
x = x[:samples]
y = y[:samples]
rng = np.random.default_rng(42)  # Constant Random Seed
mask = rng.random(samples)
train_mask = mask < 0.8  # Train/test split
test_mask = ~train_mask
x_train, y_train = x[train_mask], y[train_mask]
x_test, y_test = x[test_mask], y[test_mask]

BATCH_SIZE = 1024
VOCAB_SIZE = 5000
EPOCHS = 3
encoder = keras.layers.TextVectorization(VOCAB_SIZE)
encoder.adapt(x_train[:50_000])
model = keras.Sequential([
    encoder,
    keras.layers.Embedding(input_dim=len(encoder.get_vocabulary()), output_dim=16, mask_zero=True),
    keras.layers.Bidirectional(keras.layers.LSTM(16)),
    keras.layers.Dense(16, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])
model.compile(loss=keras.losses.BinaryCrossentropy(from_logits=False),
    optimizer=keras.optimizers.Adam(1e-3),
    metrics=['accuracy']
)

ltsm1 = model.fit(x_train, y_train, epochs=EPOCHS, batch_size=BATCH_SIZE, validation_data=(x_test, y_test), validation_steps=30)
model.summary()


text = [("Ходили с семьёй, фильм отличный, рекомендуем к просмотру :D!"),
        ("Редкостная фигня, я разочарован, зачем вообще такое снимать :((( ??")]


print(f'1: "{np.array(text)[0]}"\n')
print(f'2: "{np.array(text)[1]}"\n')

predLTSM = model.predict(np.array(text))
print(f'\nLSTM 1: Уровень позитивности {predLTSM[0][0] * 100 // 0.1 / 10} %\n')
print(f'\nLSTM 2: Уровень позитивности {predLTSM[1][0] * 100 // 0.1 / 10} %\n')

model.export('lstm_export')
np.save('lstm.voc.npy', encoder.get_vocabulary())
