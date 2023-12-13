import sys


def diff_lines(up, down, n_diff):
    out = 0
    for i, u in enumerate(up):
        if u != down[i]:
            out += 1
            if out > n_diff:
                return out
    return out


def is_mirror(mapa, idx, n_diff):
    diff = 0
    for j in range(0, idx + 1):
        up = idx - j
        if up < 0:
            break
        down = idx + j + 1
        if down > (len(mapa) - 1):
            break
        diff += diff_lines(mapa[up], mapa[down], n_diff)
        if diff > n_diff:
            return False
    return diff == n_diff


def calc_mirror_line(mapa, n_diff):
    out = 0
    for idx in range(0, len(mapa) - 1):
        if is_mirror(mapa, idx, n_diff):
            out += idx + 1
    return out


def mapa_transpose(mapa):
    mapa = tuple("".join([m[i] for m in mapa]) for i in range(len(mapa[0])))
    return mapa


def calc_value(mapa, n_diff):
    mapa = mapa.splitlines()
    mapa = tuple(map(str.strip, mapa))
    out = 100 * calc_mirror_line(mapa, n_diff)
    mapa = mapa_transpose(mapa)
    out += calc_mirror_line(mapa, n_diff)
    return out


maps = sys.stdin.read().split("\n\n")

vals = map(lambda x: calc_value(x, 0), maps)
print("Part 1:", sum(vals))
vals = map(lambda x: calc_value(x, 1), maps)
print("Part 2:", sum(vals))
