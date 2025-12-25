import sys


def get_tile(line):
    a, b = line.split(",")
    return complex(int(a), int(b))


def part1(tiles):
    areas = list()
    for x, a in enumerate(tiles):
        for b in tiles[x + 1 :]:
            areas.append((abs(a.real - b.real) + 1) * (abs(a.imag - b.imag) + 1))
    return int(max(areas))


def get_borders(tiles):
    out = set()
    for x, a in enumerate(tiles[:-1]):
        b = tiles[x + 1]
        diff = b - a
        op = diff / abs(diff)
        while a != b:
            out.add(a)
            a += op
        out.add(b)
    return out


def is_in(center, borders):
    n_border = 0
    while center.real != -1:
        if center in borders:
            n_border += 1
        center -= 1
    return (n_border % 2) == 1


def no_cross(tl, br, borders):
    i = (tl.imag + br.imag) // 2
    for r in range(int(tl.real + 1), int(br.real)):
        if complex(r, i) in borders:
            return False
    r = (tl.real + br.real) // 2
    for i in range(int(tl.imag + 1), int(br.imag)):
        if complex(r, i) in borders:
            return False
    return True


def part2(tiles):
    borders = get_borders(tiles)
    max_area = 0
    for x, a in enumerate(tiles):
        for b in tiles[x + 1 :]:
            min_r = min(a.real, b.real)
            max_r = max(a.real, b.real)
            min_i = min(a.imag, b.imag)
            max_i = max(a.imag, b.imag)
            for c in tiles:
                if (
                    c.real > min_r
                    and c.real < max_r
                    and c.imag > min_i
                    and c.imag < max_i
                ):
                    break
            else:
                area = (abs(a.real - b.real) + 1) * (abs(a.imag - b.imag) + 1)
                if area < max_area:
                    continue

                if not is_in(complex(min_r + 1, min_i + 1), borders):
                    continue
                if not no_cross(complex(min_r, min_i), complex(max_r, max_i), borders):
                    continue

                max_area = max(area, max_area)

    return int(max_area)


tiles = tuple(map(get_tile, sys.stdin.readlines()))
print("Part 1:", part1(tiles))
print("Part 2:", part2(tiles))
