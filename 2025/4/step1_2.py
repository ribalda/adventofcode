import sys


def parse_world(lines):
    out = dict()
    for x, line in enumerate(lines):
        for y, v in enumerate(line.strip()):
            out[complex(x, y)] = v
    return out


def get_neighbours(world, pos):
    for i in range(-1, 2):
        for j in range(-1, 2):
            new_pos = pos + complex(i, j)
            if new_pos in world and new_pos != pos:
                yield world[new_pos]


def part1(world):
    out = 0
    for p in world:
        if world[p] != "@":
            continue
        if list(get_neighbours(world, p)).count("@") <= 3:
            out += 1
    return out


def part2(world):
    out = 0
    done = False
    while not done:
        done = True
        new_world = dict()
        for p in world:
            new_world[p] = world[p]
            if world[p] != "@":
                continue
            if list(get_neighbours(world, p)).count("@") <= 3:
                out += 1
                done = False
                new_world[p] = "."
        world = new_world
    return out


world = parse_world(sys.stdin.readlines())
print("Part 1:", part1(world))
print("Part 2:", part2(world))
