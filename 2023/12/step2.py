import sys
from functools import lru_cache


@lru_cache(maxsize=None)
def get_combos(record, crc):
    if len(crc) == 0:
        if record.count('#') != 0:
            return 0
        return 1
    if len(record) == 0:
        return 0

    if record[0] == ".":
        return get_combos(record[1:], crc)

    if record[0] == "#":
        len_h = crc[0]
        for i in range(len_h):
            if i >= len(record):
                return 0
            if record[i] == ".":
                return 0
        if len_h < len(record) and record[len_h] == "#":
            return 0

        return get_combos(record[crc[0] + 1 :], crc[1:])

    dot_count = get_combos("." + record[1:], crc)
    hash_count = get_combos("#" + record[1:], crc)
    return dot_count + hash_count


def get_combinations(line, multi):
    record, crc = line.split()

    record = (multi - 1) * (record + "?") + record
    crc = (multi - 1) * (crc + ",") + crc

    crc = tuple(map(int, crc.split(",")))
    combos = get_combos(record, crc)
    return combos


lines = sys.stdin.readlines()
print("Part 1:", sum(map(lambda x: get_combinations(x, 1), lines)))
print("Part 2:", sum(map(lambda x: get_combinations(x, 5), lines)))
