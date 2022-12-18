import sys
from collections import deque


def around(cube):
    out = []
    for i in range(len(cube)):
        for j in [-1, +1]:
            cube2 = list(cube)
            cube2[i] += j
            out.append(tuple(cube2))
    return out


def find_air(cubes):
    minair = []
    maxair = []
    for i in range(len(list(cubes)[0])):
        minair.append(min([x[i] for x in cubes]) - 1)
        maxair.append(max([x[i] for x in cubes]) + 1)

    air = {tuple(minair)}
    todo = deque([tuple(minair)])
    while todo:
        t = todo.popleft()
        for c in around(t):
            if c in cubes or c in air:
                continue
            for i in range(len(minair)):
                if c[i] < minair[i] or c[i] > maxair[i]:
                    break
            else:
                air.add(c)
                todo.append(c)
    return air


cubes = set()
border_count = 0
for l in sys.stdin.readlines():
    coord = list(map(int, l.split(",")))
    cubes.add(tuple(coord))


air = find_air(cubes)

outside_border = 0
all_border = 0
for coord in cubes:
    for c in around(coord):
        if c in cubes:
            continue
        all_border += 1
        if c in air:
            outside_border += 1

print("Step1", all_border, "Step2", outside_border)
