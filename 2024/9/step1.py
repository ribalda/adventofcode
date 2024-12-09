import sys
from collections import deque


def crc(files):
    # print(files)
    out = 0
    for i, v in enumerate(files):
        out += i * v
    return out


def fill_hole(disk, out, len_hole, last):
    last_num, n_last = last
    while len_hole:
        if n_last == 0:
            if not disk:
                return (last_num, n_last)
            n_last = disk.pop()
            last_num = last_num - 1
            if disk:
                disk.pop()
        to_write = min(len_hole, n_last)
        out.extend(to_write * [last_num])
        n_last -= to_write
        len_hole -= to_write

    return last_num, n_last


def decompress(disk):
    if (len(disk) % 2) == 0:
        disk.pop()
    first_num = 0
    last = ((len(disk) // 2 + 1), 0)
    out = deque([])
    while disk:
        n_first = disk.popleft()
        out.extend(n_first * [first_num])
        first_num += 1
        if not disk:
            continue
        len_hole = disk.popleft()
        last = fill_hole(disk, out, len_hole, last)
    out.extend(last[1] * [last[0]])
    return out


disk = deque(map(int, sys.stdin.readline().strip()))
out = decompress(disk)
print("Step 1:", crc(out))
