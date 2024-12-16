import sys
import heapq


def next(cost, pos, dir):
    yield cost + 1, pos + dir, dir
    yield cost + 1000, pos, dir * 1j
    yield cost + 1000, pos, dir * -1j
    yield cost + 2000, pos, dir * -1


def find_cost(world, start, end):
    visited = dict()
    dummy = 0
    todo = []
    heapq.heappush(todo, (0, dummy, set(), start, 1j))
    end_cost = None
    while todo:
        cost, _, positions, pos, dir = heapq.heappop(todo)

        if end_cost and cost > end_cost:
            break

        if (pos, dir) not in visited:
            visited[(pos, dir)] = (cost, positions)
        else:
            if visited[(pos, dir)][0] < cost:
                continue

            new_visited = visited[pos, dir][1] | positions
            if new_visited == visited[(pos, dir)][1]:
                continue
            visited[(pos, dir)] = (cost, new_visited)

        if pos == end:
            end_cost = cost
            continue

        for new_cost, new_pos, new_dir in next(cost, pos, dir):
            dummy += 1
            if world[new_pos] == "#":
                continue
            heapq.heappush(
                todo, (new_cost, dummy, positions | set((pos,)), new_pos, new_dir)
            )

    out = set([end])
    for d in -1, 1, -1j, 1j:
        if (end, d) in visited:
            out |= visited[(end, d)][1]

    return end_cost, len(out)


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

p1, p2 = find_cost(world, start, end)
print("Part 1:", p1)
print("Part 2:", p2)
