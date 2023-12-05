import sys


def parse_range(rang):
    t, f, l = map(int, rang.strip().split())
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


def parse_seeds(seeds):
    out = []
    for s in range(0, len(seeds), 2):
        out.append((seeds[s], seeds[s + 1]))
    return out


def travel_ranges(seeds, roads):
    ranges_in = seeds
    ranges_out = []
    while ranges_in:
        range_start, range_len = ranges_in.pop()
        for road_start, road_len, road_offset in roads:
            if road_start in range(range_start + 1, range_start + range_len):
                l = road_start - range_start
                ranges_in.append((range_start, l))
                range_start += l
                range_len -= l
            if road_start + road_len - 1 in range(
                range_start, range_start + range_len - 1
            ):
                l = range_start + range_len - (road_start + road_len)
                ranges_in.append((road_start + road_len, l))
                range_len -= l
            if range_start in range(road_start, road_start + road_len):
                ranges_out.append((range_start + road_offset, range_len))
                break
        else:
            ranges_out.append((range_start, range_len))
    return ranges_out


def travel_mapa(seeds, mapa):
    for r in mapa:
        seeds = travel_ranges(seeds, r)
    return seeds


seeds_mapa = sys.stdin.read().split("\n\n")
seeds = list(map(int, seeds_mapa[0].split(": ")[1].split()))
seeds = parse_seeds(seeds)
mapa = list(map(parse_road, seeds_mapa[1:]))

out = travel_mapa(seeds, mapa)
print(min(out)[0])
