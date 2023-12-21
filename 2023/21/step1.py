import sys
from collections import deque, defaultdict

lines = sys.stdin.readlines()

mapa = {}
for idx, line in enumerate(lines):
    for jdx, v in enumerate(line.strip()):
        pos = complex(idx, jdx)
        if v == "S":
            start = pos
            v = "."
        mapa[pos] = v

todo = deque([(0, start)])
added = defaultdict(set)
added[0].add(start)


end = 64

while todo:
    steps, pos = todo.popleft()
    next_step = steps + 1
    if next_step > end:
        continue
    for d in (complex(0, 1), complex(0, -1), complex(1, 0), complex(-1, 0)):
        next_pos = pos + d
        if next_pos in added[next_step]:
            continue
        if next_pos not in mapa:
            continue
        if mapa[next_pos] != ".":
            continue
        todo.append((next_step, next_pos))
        added[next_step].add(next_pos)

print("Step 1:", len(added[end]))
