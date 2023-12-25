import sys
import random


def remove_one_link(cities, roads):
    lucky = random.randint(0, len(roads) - 1)
    fr, to = roads[lucky]

    # kill to
    cities[fr] += cities[to]
    del cities[to]

    roads_out = []
    for r in roads:
        if r == (to, fr) or r == (fr, to):
            continue
        r_f, r_t = r
        if r_f == to:
            r_f = fr
        if r_t == to:
            r_t = fr
        roads_out.append((r_f, r_t))
    return roads_out


def compact(cities_in, roads, n_cities, n_roads):
    roads = roads.copy()
    cities = dict()
    for city in cities_in:
        cities[city] = 1

    while len(cities) != n_cities:
        roads = remove_one_link(cities, roads)

    if len(roads) != n_roads:
        return None

    out = 1
    for v in cities.values():
        out *= v
    return out


def find_groups(cities, roads):
    while True:
        len_part = compact(cities, roads, 2, 3)
        if len_part != None:
            return len_part


cities = set()
roads = []
for line in sys.stdin.readlines():
    line = line.strip()
    fr, tos = line.split(": ")
    tos = tos.split(" ")
    cities.add(fr)
    for to in tos:
        cities.add(to)
        roads.append((fr, to))

print("Part 1:", find_groups(cities, roads))
