import tb
import lxml.etree
import io
from PIL import Image
import keras
import numpy as np

# image labels -> CIFAR10
cifar10_labels_map = {
    'aeroplane': 'airplane',
    'bird': 'bird',
    'bus': 'truck',
    'train': 'truck',
    'boat': 'ship',
    'cat': 'cat',
    'car': 'automobile',
    'bicycle': 'automobile',
    'motorbike': 'automobile',
    'cow': 'deer',
    'sheep': 'deer',
    'dog': 'dog',
    'horse': 'horse',
    'ship': 'ship',
    'truck': 'truck',
}

cifar10_order = [
    'airplane',
    'automobile',
    'bird',
    'cat',
    'deer',
    'dog',
    'frog',
    'horse',
    'ship',
    'truck',
]

label_to_idx = {l: i for i, l in enumerate(cifar10_order)}

predictor = keras.models.load_model('/home/guest/keras-cifar10-2.keras')

xp_objects = lxml.etree.XPath('/annotation/object')
xp_name    = lxml.etree.XPath('name/text()')
xp_xmin    = lxml.etree.XPath('bndbox/xmin/text()')
xp_ymin    = lxml.etree.XPath('bndbox/ymin/text()')
xp_xmax    = lxml.etree.XPath('bndbox/xmax/text()')
xp_ymax    = lxml.etree.XPath('bndbox/ymax/text()')

while True:
    try:
        xml_bytes, jpg_bytes = tb.read(2)
        parsed = lxml.etree.XML(xml_bytes)
        image = Image.open(io.BytesIO(jpg_bytes)).convert('RGB')

        for obj in xp_objects(parsed):
            names = xp_name(obj)
            if not names:
                continue
            name = names[0]
            if name not in cifar10_labels_map:
                continue

            gt_label = cifar10_labels_map[name]

            xmin = int(xp_xmin(obj)[0])
            ymin = int(xp_ymin(obj)[0])
            xmax = int(xp_xmax(obj)[0])
            ymax = int(xp_ymax(obj)[0])

            crop = image.crop((xmin, ymin, xmax, ymax))
            crop = crop.resize((32, 32))

            arr = keras.utils.img_to_array(crop)
            arr = np.expand_dims(arr, axis=0)

            preds = predictor.predict(arr, verbose=0)
            pred_idx = int(np.argmax(preds[0]))
            pred_label = cifar10_order[pred_idx]

            # true_label pred_label
            print(f"{gt_label}\t{pred_label}")

    except Exception:
        break
