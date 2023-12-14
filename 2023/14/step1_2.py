import sys


def print_map(mapa):
    for m in mapa:
        print("".join(m))
    print()


def value_map(mapa):
    out = 0
    for idx, line in enumerate(mapa):
        for _, v in enumerate(line):
            if v == "O":
                out += len(mapa) - idx
    return out


def slide_north(mapa):
    lines = list(map(list, mapa))
    for idx, line in enumerate(lines[:-1]):
        for jdx, v in enumerate(line):
            if v != ".":
                continue
            for south in range(idx + 1, len(lines)):
                if lines[south][jdx] == "#":
                    break
                if lines[south][jdx] == "O":
                    lines[idx][jdx] = "O"
                    lines[south][jdx] = "."
                    break
    return tuple(map(tuple, lines))


def rotate_map(mapa):
    lines = list(map(list, mapa))
    lines.reverse()
    lines = [[l[i] for l in lines] for i in range(len(lines))]
    return tuple(map(tuple, lines))


def slide_cycle(mapa):
    for _ in range(4):
        mapa = slide_north(mapa)
        mapa = rotate_map(mapa)
    return mapa


def slide_cycle_n(mapa, n):
    map_idx = {}
    maps = []
    for i in range(n):
        if mapa in map_idx:
            cycle_len = i - map_idx[mapa]
            pos = (n - i) % cycle_len
            pos += map_idx[mapa]
            return maps[pos]
        map_idx[mapa] = i
        maps.append(mapa)
        mapa = slide_cycle(mapa)
        i += 1
    return 0


lines = sys.stdin.readlines()
lines = map(str.strip, lines)
lines = map(tuple, lines)
mapa = tuple(lines)

print("Part 1:", value_map(slide_north(mapa)))
print("Part 2:", value_map(slide_cycle_n(mapa, 1000000000)))
