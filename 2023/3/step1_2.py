import sys


def get_num(lines, i, j0, numbers, numbers_start):
    val = 0
    j = j0
    while ord(lines[i][j]) in range(ord("0"), ord("9") + 1):
        val *= 10
        val += int(lines[i][j])
        numbers_start[complex(i, j)] = complex(i, j0)
        j += 1

    numbers[complex(i, j0)] = val
    return j - j0


def get_adj(pos, numbers, numbers_start):
    out = set()
    for i in -1, 0, 1:
        for j in -1, 0, 1:
            p = complex(pos.real + i, pos.imag + j)
            if p in numbers_start:
                start = numbers_start[p]
                out.add((start, numbers[start]))
    return out


lines = sys.stdin.readlines()
part = dict()
numbers = dict()
numbers_start = dict()
for i, l in enumerate(lines):
    j = 0
    while j < len(l) - 1:
        c = l[j]
        if c == ".":
            j += 1
            continue
        if ord(c) in range(ord("0"), ord("9") + 1):
            j += get_num(lines, i, j, numbers, numbers_start)
            continue
        part[complex(i, j)] = c
        j += 1

part1_numbers = set()
part2_sum = 0
for n in part:
    adj = get_adj(n, numbers, numbers_start)
    part1_numbers |= adj
    if part[n] == "*" and len(adj) == 2:
        adj = list(adj)
        part2_sum += adj[0][1] * adj[1][1]

part1_sum = 0
for n in part1_numbers:
    part1_sum += n[1]
print("Part1:", part1_sum)
print("Part2:", part2_sum)
