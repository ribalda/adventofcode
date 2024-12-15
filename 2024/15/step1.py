import sys


def move(world, pos, m):
    new_pos = pos + m

    if world[new_pos] == "#":
        return pos
    if world[new_pos] == "O":
        move(world, new_pos, m)
    if world[new_pos] == ".":
        world[new_pos] = world[pos]
        world[pos] = "."
        return new_pos
    return pos


def sum_gps(world):
    out = 0
    for p in world:
        if world[p] == "O":
            out += p.real * 100 + p.imag

    return int(out)


p1, p2 = sys.stdin.read().split("\n\n")
moves = "".join([x.strip() for x in p2.splitlines()])
world = dict()
for x, line in enumerate(p1.splitlines()):
    for y, val in enumerate(line):
        world[complex(x, y)] = val
        if val == "@":
            world[complex(x, y)] = "."
            pos = complex(x, y)

for m in moves:
    m = {
        "<": complex(0, -1),
        ">": complex(0, 1),
        "^": complex(-1, 0),
        "v": complex(1, 0),
    }[m]
    pos = move(world, pos, m)


print("Part 1:", sum_gps(world))
