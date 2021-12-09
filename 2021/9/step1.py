import sys

mapa = []
for line in sys.stdin.readlines():
    line = list(map(int, list(line.strip())))
    mapa.append(line)


low_sum = 0
for i in range(len(mapa)):
    for j in range(len(mapa[i])):
        for p in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            n_i = i + p[0]
            n_j = j + p[1]
            if n_i < 0 or n_j < 0 or n_i >= len(mapa) or n_j >= len(mapa[i]):
                continue
            if mapa[i][j] >= mapa[n_i][n_j]:
                break
        else:
            low_sum += mapa[i][j] + 1

print(low_sum)
