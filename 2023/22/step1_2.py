import sys
import bisect


def get_rock(line):
    left_right = line.strip().split("~")
    left_right = list(map(lambda x: x.split(","), left_right))
    out = tuple()
    for dim in range(3):
        a_b = [left_right[0][dim], left_right[1][dim]]
        a_b = list(map(int, a_b))

        out += (range(min(a_b), max(a_b) + 1),)
    return out


def collide(a, b):
    for i in range(len(a)):
        if a[i][0] < b[i][0]:
            x_y = [a[i], b[i]]
        else:
            x_y = [b[i], a[i]]
        if x_y[1][0] > x_y[0][-1]:
            return False
    return True


def print_rocks(rocks):
    for r in rocks:
        print(r)
    print()


def fall_rocks(rocks, pos = None):
    n_fall = 0
    rocks.sort(key=lambda x: x[-1][0])
    out = []

    for i in rocks:
        if pos:
            if pos == i:
                pos = None
                continue
            bisect.insort(out, i, key=lambda x: -x[-1][-1])
            continue
        
        for o in out:
            if collide(i[:2], o[:2]):
                z = o[-1][-1] + 1
                break
        else:
            z = 1

        if z != i[-1][0]:
            n_fall += 1

        r = (i[0:2]) + (range(z, z + len(i[-1])),)
        bisect.insort(out, r, key=lambda x: -x[-1][-1])
    return n_fall, out


def get_pillars(rocks):
    pillars = set()
    for a in rocks:
        bellow = None
        for b in rocks:
            if a == b:
                continue
            if b[-1][-1] + 1 != a[-1][0]:
                continue
            if not collide(a[:2], b[:2]):
                continue
            if bellow:
                bellow = None
                break
            bellow = b
        if bellow:
            pillars.add(bellow)
    return pillars


def calc_above(rocks, p_in):
    n_fall, _ = fall_rocks(rocks, p_in)

    return n_fall


lines = sys.stdin.readlines()
rocks = list(map(get_rock, lines))
_, rocks = fall_rocks(rocks)
pillars = get_pillars(rocks)
print("Part 1:", len(rocks) - len(pillars))
print("Part 2:", sum([calc_above(rocks, p) for p in pillars]))
