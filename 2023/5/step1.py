import sys


def parse_range(rang):
    t, f, l = map(int, rang.split())
    return (f, l, t - f)


def parse_road(road):
    return list(map(parse_range, road.splitlines()[1:]))


def travel(seed, roads):
    for ro in roads:
        for f, l, o in ro:
            if seed >= f and seed < f + l:
                seed += o
                break
    return seed


seeds_mapa = sys.stdin.read().split("\n\n")
seeds = list(map(int, seeds_mapa[0].split(": ")[1].split()))
ranges = list(map(parse_road, seeds_mapa[1:]))

dests = list(map(lambda x: travel(x, ranges), seeds))
print(min(dests))
