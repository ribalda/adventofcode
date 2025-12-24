import sys


def parse_ranges(ranges):
    out = list()
    for r in ranges.splitlines():
        a, b = r.split("-")
        out.append(tuple((int(a), int(b))))
    return tuple(out)


def part1(ranges, products):
    out = 0
    for p in products:
        for a, b in ranges:
            if p >= a and p <= b:
                out += 1
                break
    return out


def reduce_ranges(ranges):
    out = list()
    for i, (a1, b1) in enumerate(ranges):
        for a2, b2 in ranges[i + 1 :]:
            if a1 >= a2 and b1 <= b2:
                break
            if a1 >= a2 and a1 <= b2:
                a1 = b2 + 1
            if b1 >= a2 and b1 <= b2:
                b1 = a2 - 1
        else:
            out.append((a1, b1))
    return tuple(out)


def part2(ranges):
    ranges = reduce_ranges(ranges)
    ranges = reduce_ranges(ranges[::-1])
    s = 0
    for a1, b1 in ranges:
        s += b1 - a1 + 1
    return s


ranges, products = sys.stdin.read().split("\n\n")

ranges = parse_ranges(ranges)
products = tuple(map(int, products.splitlines()))

print("Part 1:", part1(ranges, products))
print("Part 2:", part2(ranges))
