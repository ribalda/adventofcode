import sys


def get_world(txt):
    out = dict()
    for l, line in enumerate(txt.splitlines()):
        for c, val in enumerate(line):
            out[complex(l, c)] = val
    return out


def enum_movements():
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if (x, y) == (0, 0):
                continue
            yield complex(x, y)


def count_words_pos(world, pos):
    out = 0
    for m in enum_movements():
        new_pos = pos
        for i in range(len("XMAS")):
            if new_pos not in world:
                break
            if world[new_pos] != "XMAS"[i]:
                break
            new_pos += m
        else:
            out += 1
    return out


def count_words(world):
    out = 0
    for p in world:
        out += count_words_pos(world, p)
    return out


def is_cross_pos(world, pos):
    if world[pos] != "A":
        return False

    for group in (complex(-1, -1), complex(1, 1)), (complex(-1, 1), complex(1, -1)):
        val = ""
        for i in group:
            new_pos = pos + i
            if new_pos not in world:
                return False
            val += world[new_pos]
        if val not in ("MS", "SM"):
            return False
    return True


def count_cross(world):
    out = 0
    for p in world:
        out += is_cross_pos(world, p)
    return out


txt = sys.stdin.read()
world = get_world(txt)
print("Step 1:", count_words(world))
print("Step 2:", count_cross(world))
