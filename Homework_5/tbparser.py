import csv
import tb

src = 'negative-ru.csv'
dst = 'test.tb'

def parse_cell(s: str):
    s = s.strip()
    try:
        return int(s)
    except ValueError:
        return s

with open(dst, 'wb') as out:
    with open(src, 'r', encoding='utf8', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            for elem in row:
                elem = elem.strip()
                try:
                    value = int(elem)
                except ValueError:
                    value = elem
                tb.write(value)