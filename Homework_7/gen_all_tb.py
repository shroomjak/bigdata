import tb
import os

directory = '/home/guest/sample/'
jpgs  = sorted(f for f in os.listdir(directory) if f.endswith('.jpg'))
xmls  = sorted(f for f in os.listdir(directory) if f.endswith('.xml'))

for x, j in zip(xmls, jpgs):
    with open(os.path.join(directory, x), 'rb') as xf, \
         open(os.path.join(directory, j), 'rb') as jf:
        tb.write(xf.read(), jf.read())
