import sys
import string
import heapq


def dist(a, b):
    return (a.real - b.real) ** 2 + (a.imag - b.imag) ** 2


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

center = complex(L / 2, C / 2)

gate = dict()
for t in tele:
    aux = tele[t]
    aux.sort(key=lambda x: dist(x, center))
    gate[aux[0]] = aux[1], +1
    gate[aux[1]] = aux[0], -1


todo = []
heapq.heappush(todo, (0, start.real, start.imag, 0))
visited = dict()
visited[start, 0] = 0
while todo:
    steps, x, y, level = heapq.heappop(todo)
    p = complex(x, y)
    if p == end and level == 0:
        print(steps)
        break
    steps2 = steps + 1
    to_try = []
    for d in (-1, 1, -1j, 1j):
        to_try.append((p + d, level))
    if p in gate:
        to_try.append((gate[p][0], level + gate[p][1]))
    for tr in to_try:
        p2 = tr[0]
        level2 = tr[1]
        if p2 == end and level2 == 0:
            print(steps2)
            sys.exit(0)
        if p2 not in mapa:
            continue
        if level2 < 0:
            continue
        if mapa[p2] != ".":
            continue
        if tr in visited and visited[tr] <= steps2:
            continue
        visited[tr] = steps2
        heapq.heappush(todo, (steps2, p2.real, p2.imag, level2))
