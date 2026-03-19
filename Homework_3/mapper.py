# for direct using ./mapper.py
# instead of python3 ./mapper.py
#!/usr/bin/env python3
import sys

try:
    for line in sys.stdin:
        data = line.strip().split(',')
        print(','.join(data[10:12])) # pickup_longitude, pickup_latitude
except EOFError:
    pass
