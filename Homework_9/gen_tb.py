import csv
import sys
import tb

reader = csv.DictReader(sys.stdin)

for row in reader:
    rec_id = row.get('id', '')
    article = row.get('article', '')
    highlights = row.get('highlights', '')
    #id (str), article (str), highlights (str)
    tb.write(rec_id, article, highlights)