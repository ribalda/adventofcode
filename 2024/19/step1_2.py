import re
import sys
from functools import cache


@cache
def count_design(patterns, design):
    if design == "":
        return 1
    out = 0
    for p in patterns:
        if design.startswith(p):
            out += count_design(patterns, design[len(p) :])
    return out


patterns, designs = sys.stdin.read().split("\n\n")

patterns = tuple(patterns.split(", "))
designs = designs.splitlines()

count = tuple(map(lambda x: count_design(patterns, x), designs))

print("Part 1:", sum(map(lambda x: x != 0, count)))
print("Part 2:", sum(count))
