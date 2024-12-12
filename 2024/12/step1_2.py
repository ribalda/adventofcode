import sys
from collections import deque


def paint(world, p, visited):
    color = world[p]
    todo = deque([p])
    borders = set()
    area = 0
    perimeter = 0
    while todo:
        p = todo.pop()
        if p in visited:
            continue
        visited.add(p)
        area += 1
        for inc in complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1):
            new_p = p + inc
            if new_p not in world or world[new_p] != color:
                borders.add(p)
                perimeter += 1
                continue
            if new_p in visited:
                continue
            todo.append(new_p)

    return calc_sides(world, borders), perimeter, area


def calc_sides_dir(world, borders, outside_dir):
    sides = 0
    visited = set()
    border_dir = outside_dir * 1j

    for b in borders:
        if b in visited:
            continue
        outside = b + outside_dir
        if outside in world and world[outside] == world[b]:
            continue
        sides += 1
        visited.add(b)
        for direction in -1, 1:
            new_pos = b
            while True:
                new_pos = new_pos + border_dir * direction
                if new_pos not in borders:
                    break
                outside = new_pos + outside_dir
                if outside in world and world[outside] == world[b]:
                    break
                visited.add(new_pos)
    return sides


def calc_sides(world, borders):
    out = 0
    for o in complex(1, 0), complex(-1, 0), complex(0, 1), complex(0, -1):
        out += calc_sides_dir(world, borders, o)
    return out


def sides_peri_area(world):
    visited = set()
    out = []
    for w in world:
        if w in visited:
            out.append((0, 0, 0))
            continue
        out.append(paint(world, w, visited))
    return out


world = dict()
for x, line in enumerate(sys.stdin.readlines()):
    for y, val in enumerate(line.strip()):
        world[complex(x, y)] = val

spa = sides_peri_area(world)

print("Step 1:", sum(map(lambda x: x[1] * x[2], spa)))
print("Step 2:", sum(map(lambda x: x[0] * x[2], spa)))
