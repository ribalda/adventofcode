import sys
from math import sqrt, prod


def parse_boxes(abc):
    return tuple(map(int, abc.split(",")))


def distance(a, b):
    out = 0
    for x, y in zip(a, b):
        out += (x - y) * (x - y)
    return sqrt(out)


def get_distances(boxes):
    out = list()
    for i, a in enumerate(boxes):
        for b in boxes[i + 1 :]:
            d = distance(a, b)
            out.append((d, a, b))
    out.sort()
    return tuple(out)


def join_box(circuits, distance):
    _, a, b = distance
    out = list()
    me = set([a, b])
    for c in circuits:
        if a not in c and b not in c:
            out.append(c)
        else:
            me |= c
    out.append(me)
    return out


def part1(boxes, n):
    distances = get_distances(boxes)
    circuits = list()
    for i in range(n):
        circuits = join_box(circuits, distances[i])

    lens = [len(x) for x in circuits]
    lens = sorted(lens)
    return prod(lens[-3:])


def part2(boxes):
    distances = get_distances(boxes)
    circuits = list()
    for d in distances:
        circuits = join_box(circuits, d)
        if len(circuits) == 1 and len(circuits[0]) == len(boxes):
            return d[1][0] * d[2][0]


boxes = tuple(map(parse_boxes, sys.stdin.readlines()))
if len(boxes) == 20:
    n = 10
else:
    n = 1000
print("Part 1:", part1(boxes, n))
print("Part 2:", part2(boxes))
