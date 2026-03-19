import sys
import csv


reader = csv.reader(sys.stdin, delimiter=';', quotechar='"')    
for fields in reader:
    if len(fields) < 4:
        continue
    text = fields[3]
    words = text.split()
    print(f"all\t{len(words)}\t1")
