import sys


def parse_elem(value):
    value = int(value)
    return [value, value >= 9]


def get_min(mapa):
    mpos = None
    mval = None
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            if mapa[i][j][1] == True:
                continue
            if not mpos:
                mpos = [i, j]
                mval = mapa[i][j][0]
            if mapa[i][j][0] < mval:
                mpos = [i, j]
                mval = mapa[i][j][0]
    return mpos


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

basins = []
while True:
    min_pos = get_min(mapa)
    if not min_pos:
        break
    b = basin_len(mapa, min_pos)
    basins.append(b)

mout = 1

for m in sorted(basins)[-3:]:
    mout *= m

print(mout)
