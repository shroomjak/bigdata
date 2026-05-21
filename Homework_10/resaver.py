import keras

model = keras.models.load_model('negpos_lstm.keras')
model.save_weights('negpos_lstm.weights.h5')

print("Модель пересохранена в формат весов")