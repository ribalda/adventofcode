import sys


def get_c(v):
    v = v.split(",")
    return complex(int(v[0]), int(v[1]))


def add_line(amap, a, b):

    if a.imag == b.imag:
        step = 1
    elif a.real == b.real:
        step = 1j
    else:
        return

    if b.imag < a.imag or b.real < a.real:
        a, b = b, a

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
