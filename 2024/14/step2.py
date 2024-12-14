from functools import reduce
import sys
import re


def pos_robot(robot, time, grid):
    out = []
    for p, v, g in zip(robot[0], robot[1], grid):
        out.append((p + v * time) % g)
    return tuple(out)


def parse_robot(line):
    m = re.match(r"p=(.*),(.*) v=(.*),(.*)", line)
    return ((int(m.group(1)), int(m.group(2))), (int(m.group(3)), int(m.group(4))))


def print_pos(pos, grid):
    pos = set(pos)
    for x in range(grid[0]):
        line = ""
        for y in range(grid[1]):
            line += "*" if (y, x) in pos else " "
        print(line)


robots = tuple(map(parse_robot, sys.stdin.readlines()))
grid = (101, 103)

i = 0
while True:
    pos = tuple(map(lambda x: pos_robot(x, i, grid), robots))
    if len(pos) == len(set(pos)):
        print_pos(pos, grid)
        break
    i += 1

print("Step 2:", i)
