import sys
import re


def map_groups(ab):
    a, b = ab.split("-")
    return range(int(a), int(b) + 1)


def is_invalid(num, is_part2):
    pattern = r"^(\d+)\1$"
    if is_part2:
        pattern = r"^(\d+)\1+$"
    m = re.search(pattern, str(num))
    if m:
        return True
    return False


def sum_invalid(r, is_part2):
    out = 0
    for i in r:
        if is_invalid(i, is_part2):
            out += i
    return out


groups = tuple(map(map_groups, sys.stdin.readline().split(",")))

print("Part 1:", sum(map(lambda x: sum_invalid(x, False), groups)))
print("Part 2:", sum(map(lambda x: sum_invalid(x, True), groups)))
