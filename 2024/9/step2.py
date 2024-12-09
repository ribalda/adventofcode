import sys
from collections import deque


def print_tri(inp):
    out = []
    for i in inp:
        val, n, space = i
        out.extend(n * [val])
        out.extend(space * ["."])
    print("".join(map(str,out)))


def crc(inp):
    i = 0
    out = 0
    for tri in inp:
        val, n, space = tri
        for _ in range(n):
            out += i * val
            i += 1
        i += space
    return out


def move_in(inp, last):
    val, n, _ = last
    for i in range(len(inp)):
        in_val, in_n, in_space = inp[i]
        if in_space >= n:
            inp[i] = (in_val, in_n, 0)
            inp.insert(i + 1, (val, n, in_space - n))
            return True

    return False


def calc_crc(disk):
    if (len(disk) % 2) != 0:
        disk.append(0)

    # val, n, n_space
    inp = []
    for i in range(len(disk) // 2):
        inp.append((i, disk[i * 2], disk[i * 2 + 1]))

    out = deque([])
    while inp:
        last = inp.pop()
        if move_in(inp, last):
            val, n, space = last
            out.appendleft((val, 0, space + n))
        else:
            out.appendleft(last)
    print_tri(out)
    return crc(out)


disk = list(map(int, sys.stdin.readline().strip()))
print("Step 2:", calc_crc(disk))
