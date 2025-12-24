import sys
from collections import deque
from functools import cache


def get_world(lines):
    out = dict()
    start = None
    for x, line in enumerate(lines):
        for y, val in enumerate(line.strip()):
            out[complex(x, y)] = val
            if val == "S":
                start = complex(x, y)
    return start, out


def part1(start, world):
    visited = set()
    todo = deque([start])
    splits = 0
    while todo:
        t = todo.popleft()
        if t in visited:
            continue
        visited.add(t)
        if world[t] == "^":
            steps = [1j, -1j]
            splits += 1
        else:
            steps = [1]
        for s in steps:
            new_t = t + s
            if new_t not in world:
                continue
            todo.append(new_t)
    return splits


def part2_slow(start, world):
    todo = deque([start])
    out = 0
    while todo:
        t = todo.popleft()
        if world[t] == "^":
            steps = [1j, -1j]
        else:
            steps = [1]
        for s in steps:
            new_t = t + s
            if new_t not in world:
                out += 1
                continue
            todo.append(new_t)
    return out


@cache
def part2(pos):
    out = 0
    if pos not in world:
        return 1
    if world[pos] == "^":
        out += part2(pos + 1j)
        out += part2(pos - 1j)
        return out
    return part2(pos + 1)


start, world = get_world(sys.stdin.readlines())
print("Part 1", part1(start, world))
print("Part 2", part2(start))
