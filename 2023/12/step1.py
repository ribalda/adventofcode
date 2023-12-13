import sys
from collections import deque
from functools import lru_cache


def print_combo(h, crc, record):
    out = ""
    pos = 0
    for idx, v in enumerate(h):
        while pos < v:
            out += "."
            pos += 1
        while pos < v + crc[idx]:
            out += "#"
            pos += 1
    while pos < len(record):
        out += "."
        pos += 1
    print(out)


@lru_cache(maxsize=None)
def sum_to_end(crc, pos):
    return sum(crc[pos:])


@lru_cache(maxsize=None)
def sum_from_start(crc, end):
    return sum(crc[:end])


@lru_cache(maxsize=None)
def sum_all(crc):
    return sum(crc)


@lru_cache(maxsize=None)
def count_hash_from(record, fr):
    return record[fr:].count("#")


@lru_cache(maxsize=None)
def min_blocks_from(record, fr):
    last = None
    out = ""
    for r in record[fr:]:
        if r != "?" and r != last:
            out += r
            last = r
    return out.count("#")


def valid_combo(h_new, crc, record):
    last_pos = h_new[-1] + crc[len(h_new) - 1]
    min_right = sum_to_end(crc, len(h_new)) + len(crc) - len(h_new)
    if last_pos + min_right > len(record):
        return False

    # Validate last hashes
    if len(h_new) == 1:
        pos = 0
    else:
        pos = h_new[-2] + crc[len(h_new) - 2]
    while pos < last_pos:
        if pos < h_new[-1]:
            if record[pos] == "#":
                return False
        else:
            if record[pos] == ".":
                return False
        pos += 1

    # Next hash is attached to us
    if last_pos < len(record) and record[last_pos] == "#":
        return False

    # Too many hashes
    if (count_hash_from(record, last_pos) + sum_from_start(crc, len(h_new))) > sum_all(
        crc
    ):
        return False

    # Not enough hashes left
    if min_blocks_from(record, last_pos) > (len(crc) - len(h_new)):
        return False

    # Extra hashes after us
    if len(h_new) == len(crc):
        while pos < len(record):
            if record[pos] == "#":
                return False
            pos +=1

    return True


def get_combos(record, crc):
    crc = tuple(map(int, crc.split(",")))
    todo = deque([()])

    out = 0
    while todo:
        h = todo.pop()
        if len(h) == 0:
            next = 0
        else:
            next = h[-1] + crc[len(h) - 1] + 1
        if min_blocks_from(record,next) > len(crc)-len(h):
            continue
        for h_start in range(next,len(record)):
            if record[h_start] == '.':
                continue
            h_new = h + (h_start,)
            if not valid_combo(h_new, crc, record):
                continue
            if len(h_new) == len(crc):
                out += 1
                # print_combo(h_new,crc,record)
                continue
            todo.append(h_new)
            if record[h_start] == '#':
                break
    return out


def get_combinations(line, multi):
    record, crc = line.split()

    record = (multi - 1) * (record + "?") + record
    crc = (multi - 1) * (crc + ",") + crc

    combos = get_combos(record, crc)
    return combos


lines = sys.stdin.readlines()
print("Part 1:", sum(map(lambda x: get_combinations(x, 1), lines)))
#print("Part 2:", sum(map(lambda x: get_combinations(x, 5), lines)))
