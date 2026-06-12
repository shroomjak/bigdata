import keras
import sys
import io
from PIL import Image
import numpy as np

predictor = keras.models.load_model('/home/guest/keras-cifar10-2.keras')

stdin_data = sys.stdin.buffer.read()
image_bytes = io.BytesIO(stdin_data)
image = Image.open(image_bytes)
input_arr = keras.utils.img_to_array(image)
verdicts = predictor.predict(np.array([input_arr]))
for image_result in verdicts:
    print(np.argmax(image_result))
