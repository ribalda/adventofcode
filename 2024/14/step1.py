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


def calc_value(pos, grid):
    out = [0, 0, 0, 0]
    for robot in pos:
        p = 0
        for i, v in enumerate(robot):
            mid = grid[i] // 2
            if v == mid:
                break
            if v > mid:
                p += 2**i
        else:
            out[p] += 1
    return reduce(lambda x, y: x * y, out)


robots = tuple(map(parse_robot, sys.stdin.readlines()))
if len(sys.argv) > 1:
    grid = (11, 7)
else:
    grid = (101, 103)


pos = tuple(map(lambda x: pos_robot(x, 100, grid), robots))
print("Step 1:",calc_value(pos, grid))
