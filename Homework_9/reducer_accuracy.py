import sys

correct = 0
total = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    parts = line.split('\t')
    gt, pred = parts
    total += 1
    if gt == pred:
        correct += 1

acc = correct / total
print(f"accuracy\t{acc:.2f}\tcorrect={correct}\ttotal={total}")