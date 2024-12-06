import sys


def walk(world, pos):
    visited = []
    fast_v = set(visited)
    while True:
        if pos in fast_v:
            return None
        visited.append(pos)
        fast_v.add(pos)
        p, d = pos
        new_p = p + d
        if new_p not in world:
            return visited
        if world[new_p] == "#":
            pos = (p, d * (complex(0, -1)))
            continue
        pos = (new_p, d)
        continue


to_dir = {
    "^": complex(-1, 0),
    "v": complex(1, 0),
    "<": complex(0, -1),
    ">": complex(0, 1),
}
world = dict()
for x, line in enumerate(sys.stdin.readlines()):
    for y, val in enumerate(line.strip()):
        world[complex(x, y)] = val
        if val in to_dir:
            start_pos = (complex(x, y), to_dir[val])

steps = walk(world, start_pos)
pos = {x[0] for x in steps}
print("Step 1:", len(pos))


n = 0
for p in pos:
    if p == start_pos[0]:
        continue
    world[p] = "#"
    if not walk(world, start_pos):
        n += 1
    world[p] = "."
print("Step 2:", n)
