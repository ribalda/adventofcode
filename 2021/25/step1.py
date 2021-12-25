import sys


def debug(mapa, lines, cols):
    for i in range(lines):
        out = ""
        for j in range(lines):
            if complex(i, j) in mapa:
                out += mapa[complex(i, j)]
            else:
                out += "."
        print(out)
    print("")


def op(mapa, v0, lines, cols):
    mov = {">": 1j, "v": 1 + 0j}
    v = v0 + mov[mapa[v0]]
    o = complex(v.real % lines, v.imag % cols)
    return o


def simulate(mapa, val, lines, cols):
    out = dict()

    n_move = 0
    for v in mapa:
        if mapa[v] != val:
            out[v] = mapa[v]
            continue

        v2 = op(mapa, v, lines, cols)
        if v2 in mapa:
            out[v] = mapa[v]
            continue
        else:
            out[v2] = mapa[v]
            n_move += 1

    return n_move, out


lines = sys.stdin.readlines()

mapa = dict()
for i, l in enumerate(lines):
    l = l.strip()
    for j, v in enumerate(l):
        if v != ".":
            mapa[complex(i, j)] = v

lines = len(lines)
cols = len(l)

runs = 0
while True:
    # print(runs)
    # debug(mapa, lines, cols)
    runs += 1
    n, mapa = simulate(mapa, ">", lines, cols)
    m, mapa = simulate(mapa, "v", lines, cols)
    if n + m == 0:
        print(runs)
        break
