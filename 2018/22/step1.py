# dest, depth = 10 + 10j, 510
dest, depth = 13 + 704j, 9465
base = 20183

mapa = dict()
for i in range(int(dest.real) + 1):
    for j in range(int(dest.imag) + 1):
        pos = complex(i, j)
        if pos == 0:
            geol = 0
        elif pos == dest:
            geol = 0
        elif j == 0:
            geol = i * 16807
        elif i == 0:
            geol = j * 48271
        else:
            geol = mapa[pos - 1j] * mapa[pos - 1]

        ero = (geol + depth) % base
        mapa[pos] = ero

res = 0
for v in mapa.values():
    res += v % 3
print(res)
