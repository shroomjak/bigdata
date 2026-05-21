import keras

model = keras.models.load_model('imdb_lstm.keras')
model.save_weights('imdb_lstm.weights.h5')

print("Модель пересохранена в формат весов")