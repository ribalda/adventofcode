import sys

DIM = 2
WORLD = range(200000000000000, 400000000000000 + 1)


def get_formula(a):
    x0, y0 = a[0][:2]
    x1, y1 = a[0][0] + a[1][0], a[0][1] + a[1][1]
    m = (y1 - y0) / (x1 - x0)
    b = y0 - (m * x0)

    if a[1][0] > 0:
        first = a[0][0]
        last = None
    elif a[1][0] == 0:
        first = a[0][0]
        last = None
    else:
        first = None
        last = a[0][0]

    return ((m, b), (first, last))


def get_point(three):
    return tuple(map(int, three.split(", ")))[:DIM]


def get_hail(line):
    hail_speed = line.split(" @ ")
    hail_speed = tuple(map(get_point, hail_speed))
    return get_formula(hail_speed)


def in_range(x, none_range):
    if none_range[0] != None:
        if x < none_range[0]:
            return False
    if none_range[1] != None:
        if x > none_range[1]:
            return False
    return True


def can_collision(a, b, world):
    (m0, b0), range0 = a
    (m1, b1), range1 = b

    if m0 == m1:
        return b0 == b1

    x_col = (b0 - b1) / (m1 - m0)
    if not in_range(x_col, range0) or not in_range(x_col, range1):
        return False

    y_col = m0 * x_col + b0

    if x_col < world[0][0] or x_col > world[0][-1]:
        return False

    if y_col < world[1][0] or y_col > world[1][-1]:
        return False
    return True


lines = sys.stdin.readlines()
hails = list(map(get_hail, lines))
world = [WORLD] * DIM

out = 0
for i in range(len(hails)):
    for j in range(i + 1, len(hails)):
        if can_collision(hails[i], hails[j], world):
            out += 1
print("Part 1:", out)
