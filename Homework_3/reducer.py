# for direct using ./reducer.py
# instead of python3 ./reducer.py
#!/usr/bin/env python3
import sys


n = 0
avg1 = 0.0
avg2 = 0.0

for line in sys.stdin:
    data = line.strip().split(',')
    try:
        x1 = float(data[0])
        x2 = float(data[1])
    except ValueError:
        continue  # skip header

    if x1 == 0 or x2 == 0:  # skip empty data lines
        continue

    n += 1
    # avg_n = (avg_{n-1} * (n-1) + x_n) / n
    avg1 = (avg1 * (n - 1) + x1) / n
    avg2 = (avg2 * (n - 1) + x2) / n

print(f'Total lines: {n}')
print(f'Mean pickup_longitude: {avg1:.6f}')
print(f'Mean pickup_latitude:  {avg2:.6f}')