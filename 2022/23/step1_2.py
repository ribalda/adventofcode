import sys
from collections import defaultdict


def print_elfs(elfs):
    lines = sorted([int(e.real) for e in elfs])
    cols = sorted([int(e.imag) for e in elfs])

    for l in range(lines[0], lines[-1] + 1):
        for c in range(cols[0], cols[-1] + 1):
            e = complex(l, c)
            if e in elfs:
                print("#", end="")
            else:
                print(".", end="")
        print("")


def around_elf(elfs, e):
    around = ((-1 - 1j), (-1), (-1 + 1j), (-1j), (1j), (1 - 1j), (1), (1 + 1j))
    out = set()
    for a in around:
        e1 = a + e
        if e1 in elfs:
            out.add(e1)
    return out


def move_elfs(elfs, movements):
    destinations = defaultdict(int)
    new_pos = dict()
    for e in elfs:
        around = around_elf(elfs, e)
        if len(around) == 0:
            new_pos[e] = e
            continue

        for move in movements:
            for m in move[1]:
                if e + m in elfs:
                    break
            else:
                e1 = e + move[0]
                destinations[e1] += 1
                new_pos[e] = e1
                break
        else:
            new_pos[e] = e

    moved = False
    new_elfs = set()
    for e in elfs:
        e1 = new_pos[e]
        if destinations[e1] == 1:
            new_elfs.add(e1)
            moved = True
        else:
            new_elfs.add(e)
    return moved, new_elfs


def free_spaces(elfs):
    lines = sorted([int(e.real) for e in elfs])
    cols = sorted([int(e.imag) for e in elfs])
    lines = lines[-1] - lines[0] + 1
    cols = cols[-1] - cols[0] + 1
    return lines * cols - len(elfs)


elfs = set()
for l, line in enumerate(sys.stdin.readlines()):
    for c, col in enumerate(line):
        if col == "#":
            elfs.add(complex(l, c))


movements = [
    (-1, (-1 - 1j, -1, -1 + 1j)),
    (1, (1 - 1j, 1, 1 + 1j)),
    (-1j, (-1 - 1j, -1j, +1 - 1j)),
    (1j, (-1 + 1j, 1j, +1 + 1j)),
]

print("Map:")
print_elfs(elfs)

moved = True
round = 0
while moved:
    round += 1
    moved, elfs = move_elfs(elfs, movements)
    if round == 10:
        print("Step1:", free_spaces(elfs))

    move = movements.pop(0)
    movements.append(move)

print("Step2:", round)
