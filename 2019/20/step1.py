import sys
import string
import heapq

mapa = dict()
lines = sys.stdin.readlines()
for i, line in enumerate(lines):
    for j, l in enumerate(line):
        mapa[complex(i, j)] = l

L = i + 1
C = j + 1

tele = dict()
for l in range(L):
    for c in range(C):
        p = complex(l, c)
        if mapa[complex(l, c)] != ".":
            continue
        dirs = -1, 1, -1j, 1j
        for d in dirs:
            name = []
            for k in range(1, 3):
                p2 = p + k * d
                if p2 not in mapa:
                    break
                if mapa[p2] not in set(string.ascii_uppercase):
                    break
                name.append(mapa[p2])
            else:
                name = "".join(sorted(name))
                if name not in tele:
                    tele[name] = []
                tele[name].append(p)

start = tele["AA"][0]
end = tele["ZZ"][0]
del tele["AA"]
del tele["ZZ"]

gate = dict()
for t in tele:
    gate[tele[t][0]] = tele[t][1]
    gate[tele[t][1]] = tele[t][0]

todo = []
heapq.heappush(todo, (0, start.real, start.imag))
visited = dict()
visited[start] = 0
while todo:
    steps, x, y = heapq.heappop(todo)
    p = complex(x, y)
    # print(steps,p)
    if p == end:
        print(steps)
        break
    steps2 = steps + 1
    to_try = []
    for d in (-1, 1, -1j, 1j):
        to_try.append(p + d)
    if p in gate:
        to_try.append(gate[p])
    for p2 in to_try:
        if p2 == end:
            print(steps2)
            sys.exit(0)
        if p2 not in mapa:
            continue
        if mapa[p2] != ".":
            continue
        if p2 in visited and visited[p2] <= steps2:
            continue
        visited[p2] = steps2
        heapq.heappush(todo, (steps2, p2.real, p2.imag))
