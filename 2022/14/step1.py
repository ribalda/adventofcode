import sys


def to_complex(v):
    v = v.split(",")
    return complex(int(v[0]), int(v[1]))


def single_dir(d):
    r = min(1, max(d.real, -1))
    i = min(1, max(d.imag, -1))
    return complex(r, i)


mapa = dict()

for l in sys.stdin.readlines():
    pos = l.split(" -> ")
    pos = list(map(to_complex, pos))
    p0 = pos[0]
    for p1 in pos[1:]:
        d1 = single_dir(p1 - p0)
        mapa[p0] = "#"
        while p0 != p1:
            p0 += d1
            mapa[p0] = "#"

eow = max([d.imag for d in mapa.keys()])

step = 0
while True:
    step += 1
    p = complex(500, 0)
    stop = False
    while not stop and p.imag <= eow:
        for s in 1j, -1 + 1j, 1 + 1j:
            if p + s not in mapa:
                p = p + s
                break
        else:
            mapa[p] = "o"
            stop = True
    if not stop:
        break
print(step - 1)
