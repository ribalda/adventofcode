import sys
from collections import defaultdict


def op(val, s):
    out = val + ord(s)
    out *= 17
    out %= 256
    return out


def hash(st):
    out = 0
    for s in st:
        out = op(out, s)
    return out


def organize_lenses(strings):
    boxes = defaultdict(list)
    for s in strings:
        if "=" in s:
            lense, val = s.split("=")
            box_n = hash(lense)
            val = int(val)
            lenses = [x[0] for x in boxes[box_n]]
            if lense not in lenses:
                boxes[box_n].append((lense, val))
                continue
            pos = [x[0] for x in boxes[box_n]].index(lense)
            boxes[box_n][pos] = (lense, val)
            continue
        lense = s[:-1]
        box_n = hash(lense)
        lenses = [x[0] for x in boxes[box_n]]
        if lense not in lenses:
            continue
        pos = [x[0] for x in boxes[box_n]].index(lense)
        del boxes[box_n][pos]
    return boxes


line = sys.stdin.readline().strip()
strings = line.split(",")
hashes = list(map(hash, strings))
print("Part 1:", sum(hashes))

boxes = organize_lenses(strings)
out = 0
for b in boxes:
    for i, (lense, val) in enumerate(boxes[b]):
        out += (b + 1) * (i + 1) * val
print("Part 2:", out)
