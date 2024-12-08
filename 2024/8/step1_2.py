import sys


def calculate_pos(world, antenna):
    out = 0
    for a in antenna:
        emiters = antenna[a]
        for i, a in enumerate(emiters):
            for b in emiters[i + 1 :]:
                for p in a + (a - b), b + (b - a):
                    if p not in world:
                        continue

                    if world[p] == "#":
                        continue
                    world[p] = "#"
                    out += 1

    return out


def calculate_emiters(world, p, dist):
    out = 0
    while p in world:
        if world[p] == "#":
            p += dist
            continue
        world[p] = "#"
        out += 1
        p += dist

    return out


def calculate_pos2(world, antenna):
    out = 0
    for a in antenna:
        emiters = antenna[a]
        for i, a in enumerate(emiters):
            for b in emiters[i + 1 :]:
                out += calculate_emiters(world, a, a - b)
                out += calculate_emiters(world, b, b - a)

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

out = calculate_pos(world.copy(), antenna)
print("Step 1:", out)
out = calculate_pos2(world.copy(), antenna)
print("Step 2:", out)
