import sys
from functools import cache


def valid_pos(dir, val):
    if val == "#":
        return False
    if val == ".":
        return True
    if dir == 1j and val == ">":
        return True
    if dir == -1j and val == "<":
        return True
    if dir == 1 + 0j and val == "v":
        return True
    if dir == -1 + 0j and val == "^":
        return True
    return False


def max_none(a, b):
    if a == None:
        return b
    if b == None:
        return a
    return max(a, b)


def inc_none(a):
    if a == None:
        return a
    return a + 1


@cache
def max_road(visited, start_pos, end_pos):
    out = None
    for dir in 1j, -1j, 1 + 0j, -1 + 0j:
        pos = start_pos + dir
        if pos not in mapa:
            continue
        if not valid_pos(dir, mapa[pos]):
            continue
        if pos in visited:
            continue
        if pos == end_pos:
            out = max_none(out, 1)
            continue
        out = max_none(out, inc_none(max_road(visited + (start_pos,), pos, end_pos)))
    return out


mapa = {}
lines = sys.stdin.readlines()
for idx, line in enumerate(lines):
    for jdx, val in enumerate(line.strip()):
        pos = complex(idx, jdx)
        if idx == 0 and val == ".":
            start_pos = pos
        if idx == len(lines) - 1 and val == ".":
            end_pos = pos
        mapa[pos] = val

sys.setrecursionlimit(1000000000)
print("Part 2:", max_road((), start_pos, end_pos))
