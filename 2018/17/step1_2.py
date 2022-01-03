import sys


def debug(mapa):
    print("***************")
    for line in range(0, max_y + 1):
        out = ""
        for col in range(min_x, max_x + 1):
            o = complex(line, col)
            if o in mapa:
                out += mapa[o]
            else:
                out += " "
        print(out)


def is_bottom_dir(mapa, p, dir):
    under = p + 1
    if under.real > max_y:
        return False
    while True:
        if p in mapa and mapa[p] == "#":
            return True
        if under not in mapa:
            return False
        if mapa[under] not in ["#", "~"]:
            return False
        p += dir
        under += dir


def is_bottom(mapa, p):
    return is_bottom_dir(mapa, p, 0 - 1j) and is_bottom_dir(mapa, p, 0 + 1j)


def paint_line(mapa, p, dir, val):
    under = p + 1
    if under.real > max_y:
        return

    while True:
        p += dir
        under += dir
        # if p.imag > max_x or p.imag < min_x:
        #    return
        if p in mapa:
            return
        mapa[p] = val
        if under not in mapa:
            return
        if mapa[under] not in ["#", "~"]:
            return


def paint(mapa, p):
    if is_bottom(mapa, p):
        o = "~"
    else:
        o = "|"
    paint_line(mapa, p, 0 - 1j, o)
    paint_line(mapa, p, 0 + 1j, o)
    mapa[p] = o


def step(mapa):
    water = []
    for p in mapa:
        if mapa[p] == "|":
            water.append(p)
    water.sort(key=lambda x: x.real, reverse=True)
    for w in water:
        w += 1
        while w not in mapa and w.real <= max_y:
            mapa[w] = "|"
            w = w + 1
        if w in mapa and mapa[w] in ["~", "#"]:
            w -= 1
            paint(mapa, w)
    return mapa


mapa = dict()
lines = sys.stdin.readlines()
for line in lines:
    first, second = line.split(", ")
    x_y, v0 = first.split("=")
    v1, v2 = second[2:].split("..")
    v0, v1, v2 = int(v0), int(v1), int(v2)
    for j in range(v1, v2 + 1):
        if x_y == "y":
            r, i = v0, j
        else:
            r, i = j, v0
        mapa[complex(r, i)] = "#"
xs = list(map(lambda x: x.imag, mapa.keys()))
ys = list(map(lambda x: x.real, mapa.keys()))
min_x = int(min(xs)) - 1
max_x = int(max(xs)) + 1
max_y = int(max(ys))
min_y = int(min(ys))

border_size = len(mapa)
debug(mapa)

mapa[complex(min_y, 500)] = "|"

while True:
    last_len = len(mapa)
    mapa = step(mapa)
    if len(mapa) == last_len:
        break
debug(mapa)
print("Step1", len(mapa) - border_size)

n_water = 0
for p in mapa:
    if mapa[p] == "|":
        n_water += 1
print("Step2", len(mapa) - border_size - n_water)
