import sys


def debug(mapa):
    for line in mapa:
        out = ""
        for l in line:
            out += str(hex(l)[-1])
        print(out)


def do_flash(mapa, fmap, i, j):
    for ii in range(i-1, i+2):
        for jj in range(j-1, j+2):
            if ii < 0 or ii >= len(mapa) or jj < 0 or jj >= len(mapa[i]) or (ii == i and jj == j):
                continue
            if fmap[ii][jj] != 0:
                continue
            mapa[ii][jj] += 1
            if mapa[ii][jj] < 10:
                continue
            fmap[ii][jj] = 1
            mapa[ii][jj] = 0
            do_flash(mapa, fmap, ii, jj)


def calc_flashes(mapa):
    fmap = []
    for i in range(len(mapa)):
        fmap.append([0] * len(mapa))
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j] != 10:
                continue
            fmap[i][j] = 1
            mapa[i][j] = 0
            do_flash(mapa, fmap, i, j)

    flashes = 0
    for i in range(len(fmap)):
        for j in range(len(fmap[i])):
            flashes += fmap[i][j]
    return flashes


def step(mapa):
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            mapa[i][j] += 1

    return calc_flashes(mapa)


mapa = []
lines = sys.stdin.readlines()
N = len(lines)

for l in lines:
    mapa.append(list(map(int, list(l.strip()))))

flashes = 0
debug(mapa)
for i in range(100):
    flashes += step(mapa)
    print(i)
    debug(mapa)


print(flashes)
