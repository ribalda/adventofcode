import sys


def walk(world, pos, visited):
    visited = dict.fromkeys(visited)
    while True:
        if pos in visited:
            return None
        visited[pos] = None
        p, d = pos
        new_p = p + d
        if new_p not in world:
            return list(visited)
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

steps = walk(world, start_pos, [])
pos = {x[0] for x in steps}
print("Step 1:", len(pos))


tested_blockers = set()
blockers = 0
for i in range(1, len(steps)):
    p, dir = steps[i]
    if p in tested_blockers:
        continue
    if p == steps[i - 1][0]:
        continue
    world[p] = "#"
    if not walk(world, steps[i - 1], steps[: i - 1]):
        blockers += 1
    world[p] = "."
    tested_blockers.add(p)
print("Step 2:", blockers)
