import sys
from collections import defaultdict


def calc_index(mapa, v):
    line, col = int(v.real), int(v.imag)
    out = 0
    for i in range(line - 1, line + 2):
        for j in range(col - 1, col + 2):
            p = complex(i, j)
            out *= 2
            out += mapa[p]
    return out


def debug(mapa, border):
    lines = range(int(border[0].real), int(border[1].real))
    cols = range(int(border[0].imag), int(border[1].imag))
    for i in lines:
        out = ""
        for j in cols:
            p = complex(i, j)
            if mapa[p] == 1:
                out += "#"
            else:
                out += "."
        print(out)
    return


def step(algo, mapa, border):
    lines = range(int(border[0].real), int(border[1].real))
    cols = range(int(border[0].imag), int(border[1].imag))
    old_border_val = mapa["dummy"]
    if old_border_val == 1:
        index = 511
    else:
        index = 0
    new_border_val = algo[index]
    out = defaultdict(lambda: new_border_val)
    for i in lines:
        for j in cols:
            p = complex(i, j)
            index = calc_index(mapa, p)
            # print("Test",p,index,algo[index])
            out[p] = algo[index]
    return out


def to_int(v):
    if v == "#":
        return 1
    return 0


mapa = defaultdict(int)
lines = sys.stdin.readlines()
for i, line in enumerate(lines[2:]):
    for j, l in enumerate(line):
        if l == "#":
            mapa[complex(i, j)] = 1


algo = list(map(to_int, list(lines[0].strip())))
border = [complex(0, 0), complex(i, j)]

for i in range(50):
    border[0] -= complex(2, 2)
    border[1] += complex(2, 2)
    mapa = step(algo, mapa, border)
    if i == 2 - 1:
        print("Step1", sum(mapa.values()))
print("Step2", sum(mapa.values()))
