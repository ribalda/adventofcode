import sys
from functools import cache

DIRS = (">", "v", "<", "^")


@cache
def next_step(p0, d0):
    m = 1j, 1, -1j, -1
    p1 = p0 + m[d0]

    if p1 in mapa:
        if mapa[p1] == ".":
            return p1, d0
        return None

    p1, d1 = teleport[p1, d0]
    if mapa[p1] == "#":
        return None
    return p1, d1


def _calc_teleport(teleport, L, p0, k0, p1, k1, d0, d1):
    for _ in range(L):
        teleport[p0, d0] = p1, d1
        p0 += k0
        p1 += k1


def calc_teleport(L):
    teleport = dict()

    # 6->2
    p0 = complex(0, L + 1)
    k0 = 1j
    p1 = complex(3 * L + 1, 1)
    k1 = 1
    _calc_teleport(teleport, L, p0, k0, p1, k1, DIRS.index("^"), DIRS.index(">"))

    # 2->6
    p0 = complex(3 * L + 1, 0)
    k0 = 1
    p1 = complex(1, L + 1)
    k1 = 1j
    _calc_teleport(teleport, L, p0, k0, p1, k1, DIRS.index("<"), DIRS.index("v"))

    # 3>2
    p0 = complex(0, 3 * L)
    k0 = -1j
    p1 = complex(4 * L, L)
    k1 = -1j
    _calc_teleport(teleport, L, p0, k0, p1, k1, DIRS.index("^"), DIRS.index("^"))

    # 2->3
    p0 = complex(4 * L + 1, L)
    k0 = -1j
    p1 = complex(1, 3 * L)
    k1 = -1j
    _calc_teleport(teleport, L, p0, k0, p1, k1, DIRS.index("v"), DIRS.index("v"))

    # 3->5
    p0 = complex(L + 1, 2 * L + 1)
    k0 = 1j
    p1 = complex(L + 1, 2 * L)
    k1 = 1
    _calc_teleport(teleport, L, p0, k0, p1, k1, DIRS.index("v"), DIRS.index("<"))

    # 5->3
    p0 = complex(L + 1, 2 * L + 1)
    k0 = 1
    p1 = complex(L, 2 * L + 1)
    k1 = +1j
    _calc_teleport(teleport, L, p0, k0, p1, k1, DIRS.index(">"), DIRS.index("^"))

    # 3->1
    p0 = complex(L, 3 * L + 1)
    k0 = -1
    p1 = complex(2 * L + 1, 2 * L)
    k1 = +1
    _calc_teleport(teleport, L, p0, k0, p1, k1, DIRS.index(">"), DIRS.index("<"))

    # 1->3
    p0 = complex(2 * L + 1, 2 * L + 1)
    k0 = +1
    p1 = complex(L, 3 * L)
    k1 = -1
    _calc_teleport(teleport, L, p0, k0, p1, k1, DIRS.index(">"), DIRS.index("<"))

    # 1->2
    p0 = complex(3 * L + 1, L + 1)
    k0 = +1j
    p1 = complex(3 * L + 1, L)
    k1 = 1
    _calc_teleport(teleport, L, p0, k0, p1, k1, DIRS.index("v"), DIRS.index("<"))

    # 2->1
    p0 = complex(3 * L + 1, L + 1)
    k0 = 1
    p1 = complex(3 * L, L + 1)
    k1 = +1j
    _calc_teleport(teleport, L, p0, k0, p1, k1, DIRS.index(">"), DIRS.index("^"))

    # 4->5
    p0 = complex(2 * L, L)
    k0 = -1j
    p1 = complex(2 * L, L + 1)
    k1 = -1
    _calc_teleport(teleport, L, p0, k0, p1, k1, DIRS.index("^"), DIRS.index(">"))

    # 5->4
    p0 = complex(2 * L, L)
    k0 = -1
    p1 = complex(2 * L + 1, L)
    k1 = -1j
    _calc_teleport(teleport, L, p0, k0, p1, k1, DIRS.index("<"), DIRS.index("v"))

    # 4->6
    p0 = complex(2 * L + 1, 0)
    k0 = 1
    p1 = complex(L, L + 1)
    k1 = -1
    _calc_teleport(teleport, L, p0, k0, p1, k1, DIRS.index("<"), DIRS.index(">"))

    # 6->4
    p0 = complex(L, L)
    k0 = -1
    p1 = complex(2 * L + 1, 1)
    k1 = 1
    _calc_teleport(teleport, L, p0, k0, p1, k1, DIRS.index("<"), DIRS.index(">"))

    return teleport


data = sys.stdin.read()
lines, path = data.split("\n\n")


mapa = dict()
p0 = None
d0 = 0
L = 0
for i, row in enumerate(lines.splitlines()):
    for j, c in enumerate(row):
        if c in (".", "#"):
            p = complex(i + 1, j + 1)
            mapa[p] = c
            if p0 == None:
                p0 = p
            L = max(L, j + 1)
L = max(L, i + 1)
L = L // 4

teleport = calc_teleport(L)

if path[-1] == "\n":
    path = path[:-1]
path = path.replace("L", " L ")
path = path.replace("R", " R ")
steps = []
for p in path.split():
    if p in ("L", "R"):
        steps.append(p)
    else:
        steps.append(int(p))

for s in steps:
    if s in ("L", "R"):
        if s == "L":
            d0 -= 1
        else:
            d0 += 1
        d0 = d0 % len(DIRS)
        continue
    for _ in range(s):
        ret = next_step(p0, d0)
        if ret == None:
            break
        p0, d0 = ret

print(int(p0.real * 1000 + p0.imag * 4 + d0))
