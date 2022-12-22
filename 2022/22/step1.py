import sys
from functools import cache

DIRS = (">", "v", "<", "^")


@cache
def next_step(p0, d0):
    m = 1j, 1, -1j, -1
    overflow = (True, True), (False, True), (True, False), (False, False)
    p1 = p0 + m[d0]

    if p1 in mapa:
        if mapa[p1] == ".":
            return p1
        return None

    do_line, do_min = overflow[d0]
    v = None
    for m in mapa:
        v1 = None
        if do_line:
            if m.real == p0.real:
                v1 = m.imag
        else:
            if m.imag == p0.imag:
                v1 = m.real
        if v1 == None:
            continue

        if v == None:
            v = v1
        if do_min:
            v = min(v1, v)
        else:
            v = max(v1, v)
    if do_line:
        p1 = complex(p1.real, v)
    else:
        p1 = complex(v, p1.imag)

    if mapa[p1] == "#":
        return None
    return p1


data = sys.stdin.read()
lines, path = data.split("\n\n")


mapa = dict()
p0 = None
d0 = 0
for i, row in enumerate(lines.splitlines()):
    for j, c in enumerate(row):
        if c in (".", "#"):
            p = complex(i + 1, j + 1)
            mapa[p] = c
            if p0 == None:
                p0 = p

if path[-1] == "\n":
    path = path[:-1]
path = path.replace("L", " L ")
path = path.replace("R", " R ")
steps = []
for p in path.split():
    if p in ("L", "R"):
        steps.append(p)
    else:
        steps.append(int(p))

for s in steps:
    if s in ("L", "R"):
        if s == "L":
            d0 -= 1
        else:
            d0 += 1
        d0 = d0 % len(DIRS)
        continue
    for _ in range(s):
        p1 = next_step(p0, d0)
        if p1 == None:
            break
        p0 = p1

print(int(p0.real * 1000 + p0.imag * 4 + d0))
