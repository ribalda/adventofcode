import sys


def dice_values():
    d = dict()
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                v = i + j + k
                if v not in d:
                    d[v] = 0
                d[v] += 1
    out = list()
    for v in d:
        out.append((v,d[v]))

    return out


def simulate(p0, p1):
    universes = dict()
    s0 = pos[0], pos[1], 0, 0, 0
    universes[s0] = 1
    wins = [0, 0]
    dice_vals = dice_values()
    while universes:
        u, n = universes.popitem()
        for v, k in dice_vals:
            p0, p1, v0, v1, w = u
            if w == 0:
                p0 = (p0 + v) % 10
                v0 += p0 + 1
                if v0 >= 21:
                    wins[0] += k * n
                    continue
                w = 1
            else:
                p1 = (p1 + v) % 10
                v1 += p1 + 1
                if v1 >= 21:
                    wins[1] += k * n
                    continue
                w = 0
            u2 = p0, p1, v0, v1, w
            if u2 not in universes:
                universes[u2] = 0
            universes[u2] += k * n
    return wins


pos = list()
for line in sys.stdin.readlines():
    pos.append((int(line.split()[4]) - 1) % 10)

print(max(simulate(pos[0], pos[1])))
