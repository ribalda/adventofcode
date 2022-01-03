import sys


def debug(mapa):
    print()
    for i in range(L):
        out = ""
        for j in range(C):
            out += mapa[complex(i, j)]
        print(out)


def around(mapa, pos):
    next = -1 - 1j, -1, -1 + 1j, -1j, 1j, 1 - 1j, 1, 1 + 1j
    ret = {"#": 0, ".": 0, "|": 0}
    for n in next:
        p = pos + n
        if p in mapa:
            ret[mapa[p]] += 1

    return ret


def cycle(mapa):
    out = dict()
    for p in mapa:
        a = around(mapa, p)
        if mapa[p] == ".":
            if a["|"] >= 3:
                out[p] = "|"
            else:
                out[p] = "."
            continue
        if mapa[p] == "|":
            if a["#"] >= 3:
                out[p] = "#"
            else:
                out[p] = "|"
            continue
        if mapa[p] == "#":
            if a["#"] >= 1 and a["|"] >= 1:
                out[p] = "#"
            else:
                out[p] = "."
            continue
    return out


mapa = dict()
lines = sys.stdin.readlines()
for i, line in enumerate(lines):
    for j, l in enumerate(line.strip()):
        mapa[complex(i, j)] = l
L = i + 1
C = j + 1

print("Step 0")
debug(mapa)
for i in range(10):
    mapa = cycle(mapa)
    print("Step", i+1)
    debug(mapa)

l = 0
t = 0
for m in mapa:
    if mapa[m] == "#":
        l += 1
    if mapa[m] == "|":
        t += 1
print(t * l)
