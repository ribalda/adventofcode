import sys


def get_around(mapa, d):
    out = {"#": 0, ".": 0}
    for m in -1, 1, -1j, 1j:
        d2 = d + m
        if d2 not in mapa:
            continue
        out[mapa[d2]] += 1
    return out


def cycle(mapa):
    out = dict()
    for d in mapa:
        around = get_around(mapa, d)
        if mapa[d] == "#":
            if around["#"] == 1:
                out[d] = "#"
            else:
                out[d] = "."
            continue
        if mapa[d] == ".":
            if around["#"] in [1, 2]:
                out[d] = "#"
            else:
                out[d] = "."
    return out


def debug(mapa):
    print("")
    for i in range(L):
        out = ""
        for j in range(L):
            out += mapa[complex(i, j)]
        print(out)


def get_rating(mapa):
    v = 0
    r = 1
    for i in range(L):
        for j in range(L):
            if mapa[complex(i, j)] == "#":
                v += r
            r <<= 1
    return v


mapa = dict()
lines = sys.stdin.readlines()
L = len(lines)
for y, line in enumerate(lines):
    for x, l in enumerate(line.strip()):
        mapa[complex(y, x)] = l

# debug(mapa)
visited = dict()
while True:
    r = get_rating(mapa)
    if r in visited:
        break
    visited[r] = True
    mapa[r] = True
    mapa = cycle(mapa)
    # debug(mapa)

debug(mapa)
print(r)
