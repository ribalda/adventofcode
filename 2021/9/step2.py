import sys


def parse_elem(value):
    value = int(value)
    return [value, value >= 9]


def get_basins(mapa):
    basins = []
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            for p in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                n_i = i + p[0]
                n_j = j + p[1]
                if n_i < 0 or n_j < 0 or n_i >= len(mapa) or n_j >= len(mapa[i]):
                    continue
                if mapa[i][j][0] >= mapa[n_i][n_j][0]:
                    break
            else:
                basins.append([i, j])
    return basins


def basin_len(mapa, min_pos):
    blen = 0
    to_visit = [min_pos]

    while len(to_visit) > 0:
        [i, j] = to_visit[0]
        to_visit = to_visit[1:]
        if mapa[i][j][1]:
            continue
        mapa[i][j][1] = True
        blen += 1
        for p in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            n_i = i + p[0]
            n_j = j + p[1]
            if n_i < 0 or n_j < 0 or n_i >= len(mapa) or n_j >= len(mapa[i]):
                continue
            if mapa[i][j] >= mapa[n_i][n_j]:
                continue
            to_visit.append([n_i, n_j])

    return blen


mapa = []
for line in sys.stdin.readlines():
    line = list(map(parse_elem, list(line.strip())))
    mapa.append(line)

basins = get_basins(mapa)
basins_len = []
for pos in basins:
    b = basin_len(mapa, pos)
    basins_len.append(b)

mout = 1
for m in sorted(basins_len)[-3:]:
    mout *= m

print(mout)
