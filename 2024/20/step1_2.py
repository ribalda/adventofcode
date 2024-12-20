import sys
import heapq


def distance(p1, p2):
    d = p1 - p2
    return abs(int(d.real)) + abs(int(d.imag))


def find_paths(dist_start, dist_end, max_cheat, max_len):
    out = 0
    for p1 in sorted(dist_start.keys(), key=lambda x: dist_start[x]):
        if dist_start[p1] > max_len:
            break
        for p2 in sorted(dist_end.keys(), key=lambda x: dist_end[x]):
            if (dist_start[p1] + dist_end[p2]) > max_len:
                break
            cheat = distance(p1, p2)
            if cheat > max_cheat:
                continue
            total_d = dist_start[p1] + distance(p1, p2) + dist_end[p2]
            if total_d <= max_len:
                out += 1
    return out


def get_next(world, pos):
    dir = 1
    for _ in range(4):
        dir *= 1j
        new_pos = pos + dir
        if new_pos not in world:
            continue
        if world[new_pos] != "#":
            yield new_pos
            continue


def get_distances(world, start):
    dist = {start: 0}
    steps = 0
    pos = start
    dummy = 0

    todo = [(steps, dummy, pos)]

    while todo:
        steps, _, pos = heapq.heappop(todo)

        new_steps = steps + 1
        for new_pos in get_next(world, pos):
            if new_pos in dist:
                if new_steps >= dist[new_pos]:
                    continue
            dist[new_pos] = new_steps
            dummy += 1
            heapq.heappush(todo, (steps + 1, dummy, new_pos))

    return dist


world = dict()
for x, line in enumerate(sys.stdin.readlines()):
    for y, val in enumerate(line.strip()):
        pos = complex(x, y)
        world[pos] = val
        if val == "S":
            start = pos
        if val == "E":
            end = pos


dist_start = get_distances(world, start)
dist_end = get_distances(world, end)


max_dist = dist_start[end] - 100
print("Part 1:", find_paths(dist_start, dist_end, 2, max_dist))
print("Part 2:", find_paths(dist_start, dist_end, 20, max_dist))
