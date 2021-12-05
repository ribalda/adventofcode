import sys


def get_c(v):
    v = v.split(",")
    return complex(int(v[0]), int(v[1]))


def add_line(amap, a, b):
    step = 0j
    if a.imag < b.imag:
        step += 1j
    if a.imag > b.imag:
        step += -1j
    if a.real < b.real:
        step += 1
    if a.real > b.real:
        step += -1

    while True:
        if a in amap:
            amap[a] += 1
        else:
            amap[a] = 1
        if a == b:
            break
        a += step
    return


amap = dict()
for line in sys.stdin.readlines():
    a, b = map(get_c, line.split("->"))
    add_line(amap, a, b)

count = 0
for pos in amap:
    if amap[pos] > 1:
        count += 1

print(count)
