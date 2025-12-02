import sys
import re


def map_groups(ab):
    a, b = ab.split("-")
    return range(int(a), int(b) + 1)


def part1_invalid(num):
    m = re.search(r"^(\d+)\1$", str(num))
    if m:
        return True
    return False


def part2_invalid(num):
    m = re.search(r"^(\d+)\1{1,}$", str(num))
    if m:
        return True
    return False


def sum_invalid(r, check):
    out = 0
    for i in r:
        if check(i):
            out += i
    return out


groups = tuple(map(map_groups, sys.stdin.readline().split(",")))

print("Part 1:", sum(map(lambda x: sum_invalid(x, part1_invalid), groups)))
print("Part 2:", sum(map(lambda x: sum_invalid(x, part2_invalid), groups)))
