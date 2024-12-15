import sys


def other(world, pos):
    if world[pos] == "]":
        return pos - 1j
    return pos + 1j


def move(world, pos, m):
    new_pos = pos + m
    # new_pos is wall?
    if world[new_pos] == "#":
        return pos

    # move left or right
    if m.imag != 0:
        if world[new_pos] in ("[", "]"):
            if move(world, new_pos, m) == new_pos:
                return pos
    # move up or down:
    elif world[new_pos] in ("[", "]"):
        if move(world.copy(), new_pos, m) == new_pos:
            return pos
        new_pos_other = other(world, new_pos)
        if move(world, new_pos_other, m) == new_pos_other:
            return pos
        move(world, new_pos, m)

    world[new_pos] = world[pos]
    world[pos] = "."
    return new_pos


def print_world(world, pos):
    for line in range(100):
        if complex(line, 0) not in world:
            break
        out = ""
        for col in range(100):
            if pos == complex(line, col):
                out += "@"
                continue

            if complex(line, col) not in world:
                break
            out += world[complex(line, col)]
        print(out)


def sum_gps(world):
    out = 0
    for p in world:
        if world[p] == "[":
            out += p.real * 100 + p.imag

    return int(out)


p1, p2 = sys.stdin.read().split("\n\n")
moves = "".join([x.strip() for x in p2.splitlines()])
world = dict()
for x, line in enumerate(p1.splitlines()):
    for y, val in enumerate(line):
        if val == "@":
            pos = complex(x, 2 * y)
            val = "."
        world[complex(x, 2 * y)] = val
        world[complex(x, 2 * y + 1)] = val
        if val == "O":
            world[complex(x, 2 * y)] = "["
            world[complex(x, 2 * y + 1)] = "]"

# print_world(world, pos)

for m in moves:
    m = {
        "<": complex(0, -1),
        ">": complex(0, 1),
        "^": complex(-1, 0),
        "v": complex(1, 0),
    }[m]
    pos = move(world, pos, m)


print("Part 2:", sum_gps(world))
