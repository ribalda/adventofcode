import sys
import heapq


def next(cost, pos, dir):
    yield cost + 1, pos + dir, dir
    yield cost + 1000, pos, dir * 1j
    yield cost + 1000, pos, dir * -1j
    yield cost + 2000, pos, dir * -1


def find_cost(world, start, end):
    visited = set()
    todo = []
    heapq.heappush(todo, (0, 0, start, 1j))
    dummy = 0
    while todo:
        cost, _, pos, dir = heapq.heappop(todo)
        visited.add((pos, dir))
        for new_cost, new_pos, new_dir in next(cost, pos, dir):
            dummy += 1
            if world[new_pos] == "#":
                continue
            if (new_pos, new_dir) in visited:
                continue
            if new_pos == end:
                return new_cost
            heapq.heappush(todo, (new_cost, dummy, new_pos, new_dir))

    return None


world = dict()
for x, line in enumerate(sys.stdin.readlines()):
    for y, val in enumerate(line.strip()):
        pos = complex(x, y)
        if val == "S":
            start = pos
            val = "."
        if val == "E":
            end = pos
            val = "."
        world[pos] = val


print("Part 1:", find_cost(world, start, end))
