import sys


def get_pos(pos, m, level):
    if pos.real < 0:
        return [(complex(1, 2), level - 1)]
    if pos.real >= L:
        return [(complex(3, 2), level - 1)]
    if pos.imag < 0:
        return [(complex(2, 1), level - 1)]
    if pos.imag >= L:
        return [(complex(2, 3), level - 1)]
    if pos == complex(2, 2):
        out = []
        if m == 1:
            for i in range(L):
                out.append((complex(0, i), level + 1))
        if m == -1:
            for i in range(L):
                out.append((complex(L-1, i), level + 1))
        if m == 1j:
            for i in range(L):
                out.append((complex(i, 0), level + 1))
        if m == -1j:
            for i in range(L):
                out.append((complex(i, L-1), level + 1))
        return out

    return [(pos, level)]


def get_around(mapa, pos):
    p, level = pos
    out = {"#": 0, ".": 0}

    for m in -1, 1, -1j, 1j:
        p2 = p + m
        for p3 in get_pos(p2, m, level):
            if p3 not in mapa:
                out["."] += 1
            else:
                out[mapa[p3]] += 1
    return out


def cycle(mapa, max_level):
    out = dict()
    for i in range(-(max_level+1), max_level+2):
        out2 = create_map(mapa, i)
        out.update(out2)
    return out


def create_map(mapa, level):
    out = dict()
    for i in range(L):
        for j in range(L):
            if (i, j) == (2, 2):
                continue
            d = complex(i, j), level
            around = get_around(mapa, d)
            if d not in mapa or mapa[d] == ".":
                if around["#"] in [1, 2]:
                    out[d] = "#"
                else:
                    out[d] = "."
                continue
            if mapa[d] == "#":
                if around["#"] == 1:
                    out[d] = "#"
                else:
                    out[d] = "."
                continue
    return out


def debug(mapa, level):
    print("")
    for i in range(L):
        out = ""
        for j in range(L):
            if (i, j) == (2, 2):
                out += "?"
            else:
                out += mapa[complex(i, j), level]
        print(out)


mapa = dict()
lines = sys.stdin.readlines()
L = len(lines)
for y, line in enumerate(lines):
    for x, l in enumerate(line.strip()):
        mapa[complex(y, x), 0] = l
del(mapa[complex(2, 2), 0])

for i in range(200):
    mapa = cycle(mapa, i)

print(len(list(filter(lambda x: x == "#", mapa.values()))))
