import sys


def map_ins(line):
    n = int(line[1:])
    if line[0] == "L":
        n *= -1
    return n


def count_cross(inss, only_last=True):
    out = 0
    new_pos = 50
    for ins in inss:
        pos = new_pos
        if ins == 0:
            continue
        new_pos = (pos + ins) % 100
        if new_pos == 0:
            out += 1
        if only_last:
            continue

        out += abs(ins) // 100

        if pos == 0 or new_pos == 0:
            continue
        if new_pos > pos and ins < 0:
            out += 1
        if new_pos < pos and ins > 0:
            out += 1

    return out


inss = tuple(map(map_ins, sys.stdin.readlines()))

print("Step 1:", count_cross(inss))
print("Step 2:", count_cross(inss, False))
