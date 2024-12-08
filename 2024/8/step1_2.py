import sys


def calculate_new_emiters1(world, p, dist):
    p += dist
    if p not in world:
        return 0
    if world[p] == "#":
        return 0
    world[p] = "#"
    return 1


def calculate_new_emiters2(world, p, dist):
    out = 0
    while p in world:
        if world[p] == "#":
            p += dist
            continue
        world[p] = "#"
        out += 1
        p += dist

    return out


def calculate_emiters(world, antenna, func):
    world = world.copy()
    out = 0
    for a in antenna:
        emiters = antenna[a]
        for i, a in enumerate(emiters):
            for b in emiters[i + 1 :]:
                out += func(world, a, a - b)
                out += func(world, b, b - a)

    return out


world = dict()
antenna = dict()

for l, line in enumerate(sys.stdin.readlines()):
    for c, val in enumerate(line.strip()):
        pos = complex(l, c)
        world[pos] = val
        if val == ".":
            continue
        if val not in antenna:
            antenna[val] = []
        antenna[val].append(pos)

out = calculate_emiters(world, antenna, calculate_new_emiters1)
print("Step 1:", out)
out = calculate_emiters(world, antenna, calculate_new_emiters2)
print("Step 2:", out)
