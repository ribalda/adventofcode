import sys


def get_range(v):
    v = v[2:]
    return tuple(map(int, v.split("..")))


def collision(a, b):
    out = []
    for i in range(len(a)):
        left = max(a[i][0], b[i][0])
        right = min(a[i][1], b[i][1])
        if right < left:
            return None
        out.append((left, right))
    return tuple(out)


def n_elem(c):
    out = 1
    for a in c:
        out *= a[1] - a[0] + 1
    return out


def sub_one(a, b):
    b = collision(a, b)
    if b == None:
        return [a]
    if a == b:
        return []
    out = []
    for i in range(len(a)):
        if a[i][0] < b[i][0]:
            o = []
            a2 = []
            for j in range(len(a)):
                if j != i:
                    a2.append(a[j])
                    o.append(a[j])
                    continue
                o.append((a[j][0], b[j][0] - 1))
                a2.append((b[j][0], a[j][1]))
            out.append(tuple(o))
            a = tuple(a2)
        if a[i][1] > b[i][1]:
            o = []
            a2 = []
            for j in range(len(a)):
                if j != i:
                    a2.append(a[j])
                    o.append(a[j])
                    continue
                o.append((b[j][1] + 1, a[j][1]))
                a2.append((a[j][0], b[j][1]))
            out.append(tuple(o))
            a = tuple(a2)
    return out


def sub_all(cuboids, b):
    out = []
    for c in cuboids:
        out += sub_one(c, b)
    return out


def calc_on(ops, world):
    cuboids = []
    for op in ops:
        o, c = op
        if world != None:
            c = collision(world, c)
        if c == None:
            continue
        cuboids = sub_all(cuboids, c)
        if o == "on":
            cuboids.append(c)

    total = 0
    for c in cuboids:
        total += n_elem(c)
    return total


ops = []
for line in sys.stdin.readlines():
    op, cuboid = line.split()
    cuboid = tuple(map(get_range, cuboid.split(",")))
    ops.append((op, cuboid))

world = ((-50, 50), (-50, 50), (-50, 50))
print("Part1", calc_on(ops, world))
print("Part2", calc_on(ops, None))
