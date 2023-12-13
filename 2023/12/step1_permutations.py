import sys
from collections import Counter
from sympy.utilities.iterables import multiset_permutations


def spring_valid(record, perm, crc):
    record_fixed = []
    idx = 0
    for r in record:
        if r == "?":
            r = perm[idx]
            idx += 1
        record_fixed += r
    record_fixed = "".join(record_fixed)
    new_crc = tuple(filter(lambda x: x != 0, map(len, record_fixed.split("."))))
    return new_crc == crc


def get_combos(record, crc):
    count = Counter(record)
    if "?" not in count:
        return 1
    n_spring = len(record)
    n_damaged = sum(crc)
    n_operational = n_spring - n_damaged
    unknown = []
    unknown += "#" * (n_damaged - count["#"])
    unknown += "." * (n_operational - count["."])
    perm = multiset_permutations(unknown)
    out = 0
    for p in perm:
        if spring_valid(record, p, crc):
            out += 1
    return out


def get_combinations(line):
    record, crc = line.split()
    crc = tuple(map(int, crc.split(",")))
    return get_combos(record, crc)


lines = sys.stdin.readlines()
print("Part 1:", sum(map(get_combinations, lines)))
