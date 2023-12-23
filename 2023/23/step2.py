import sys
import heapq
from collections import deque


def get_distances(mapa, start_pos):
    distance = {start_pos: 0}

    steps = 0
    todo = deque([])
    todo.append((steps, start_pos))
    while todo:
        t = heapq.heappop(todo)
        steps, _, pos = t
        next_steps = steps + 1
        for dir in 1j, -1j, 1 + 0j, -1 + 0j:
            next_pos = pos + dir
            if next_pos not in mapa:
                continue
            if mapa[next_pos] == "#":
                continue
            if next_pos in distance and distance[next_pos] <= next_steps:
                continue
            distance[next_pos] = next_steps
            heapq.heappush(todo, (next_steps, next_pos))
    return distance


def get_cross(mapa):
    out = set()
    for pos in mapa:
        if mapa[pos] == "#":
            continue
        count = 0
        for dir in 1j, -1j, 1 + 0j, -1 + 0j:
            next_pos = pos + dir
            if next_pos not in mapa:
                continue
            if mapa[next_pos] == "#":
                continue
            count += 1
        if count > 2:
            out.add(pos)
    return out


def get_next_cross(mapa, cross, start_pos):
    visited = set([])
    todo = deque([])
    todo.append((start_pos, visited))
    out = dict()
    while todo:
        t = todo.pop()
        pos, visited = t
        for dir in 1j, -1j, 1 + 0j, -1 + 0j:
            next_pos = pos + dir
            if next_pos == start_pos:
                continue
            if next_pos not in mapa:
                continue
            if mapa[next_pos] == "#":
                continue
            if next_pos in visited:
                continue
            if next_pos in cross:
                out[next_pos] = len(visited) + 1
                continue
            next_visited = visited.copy()
            next_visited.add(pos)
            todo.append((next_pos, next_visited))
    return out


def max_road(mapa, start_pos, end_pos):
    cross = get_cross(mapa)
    cross.add(start_pos)
    cross.add(end_pos)

    roads = dict()
    for c in cross:
        roads[c] = get_next_cross(mapa, cross, c)

    out = 0
    visited = set([start_pos])
    steps = 0
    todo = [(steps, start_pos, visited)]
    while todo:
        t = todo.pop()
        steps, pos, visited = t
        if pos == end_pos:
            out = max(out, steps)
            continue
        for next_pos in roads[pos]:
            if next_pos in visited:
                continue
            next_steps = steps + roads[pos][next_pos]
            next_visited = visited.copy()
            next_visited.add(pos)
            todo.append((next_steps, next_pos, next_visited))
    return out


mapa = {}
lines = sys.stdin.readlines()
for idx, line in enumerate(lines):
    for jdx, val in enumerate(line.strip()):
        pos = complex(idx, jdx)
        if idx == 0 and val == ".":
            start_pos = pos
        if idx == len(lines) - 1 and val == ".":
            end_pos = pos
        mapa[pos] = val

sys.setrecursionlimit(1000000000)
print("Part 2:", max_road(mapa, start_pos, end_pos))
# 6494
