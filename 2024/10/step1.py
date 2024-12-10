import sys
from collections import deque


def calc_dests(world, start_pos):
    n_dest = 0
    todo = deque([start_pos])
    visited = set(todo)
    while todo:
        pos = todo.pop()
        for inc in (complex(1, 0), complex(-1, 0), complex(0, -1), complex(0, 1)):
            new_pos = pos + inc
            if new_pos not in world:
                continue
            if new_pos in visited:
                continue
            new_val = world[new_pos]
            if new_val != world[pos] + 1:
                continue
            visited.add(new_pos)

            if new_val == 9:
                n_dest += 1
                continue
            todo.appendleft(new_pos)
    return n_dest


world = dict()
startpos = set()
for x, line in enumerate(sys.stdin.readlines()):
    for y, val in enumerate(line.strip()):
        val = int(val)
        pos = complex(x, y)
        world[pos] = val
        if val == 0:
            startpos.add(pos)

out = 0
for p in startpos:
    out += calc_dests(world, p)

print("Step 1:", out)
