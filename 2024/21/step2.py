# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

import sys
from functools import cache


def path(a, b):
    pos = {
        "7": complex(0, 0),
        "8": complex(0, 1),
        "9": complex(0, 2),
        "4": complex(1, 0),
        "5": complex(1, 1),
        "6": complex(1, 2),
        "1": complex(2, 0),
        "2": complex(2, 1),
        "3": complex(2, 2),
        "0": complex(3, 1),
        "^": complex(3, 1),
        "A": complex(3, 2),
        "<": complex(4, 0),
        "v": complex(4, 1),
        ">": complex(4, 2),
    }

    if a == b:
        return "A"

    out = ""
    dist = pos[b] - pos[a]
    if dist.real < 0:
        out += "^" * int(abs(dist.real))
    else:
        out += "v" * int(abs(dist.real))

    if dist.imag < 0:
        out += "<" * int(abs(dist.imag))
    else:
        out += ">" * int(abs(dist.imag))
    out_ver = out + "A"

    if pos[a].real == 3 and pos[b].imag == 0:
        return out_ver

    out = ""
    dist = pos[b] - pos[a]
    if dist.imag < 0:
        out += "<" * int(abs(dist.imag))
    else:
        out += ">" * int(abs(dist.imag))
    if dist.real < 0:
        out += "^" * int(abs(dist.real))
    else:
        out += "v" * int(abs(dist.real))
    out_hor = out + "A"

    if pos[a].imag == 0 and pos[b].real == 3:
        return out_hor

    # End closer to A
    if out_ver[-2] in ("^", ">"):
        return out_ver
    if out_hor[-2] in ("^", ">"):
        return out_hor
    if out_ver[-2] == "v":
        return out_ver
    if out_hor[-2] == "v":
        return out_hor

    return out_hor


@cache
def len_path_depth(a, b, depth):
    paths = path(a, b)
    if depth == 1:
        return len(paths)

    fr = "A"
    out = 0
    for t in paths:
        out += len_path_depth(fr, t, depth - 1)
        fr = t

    return out


def len_route(st_in, depth):
    out = 0
    fr = "A"
    for t in st_in:
        out += len_path_depth(fr, t, depth)
        fr = t
    return out


def calc_value(codes, n):
    out = 0
    for c in codes:
        c = c.strip()
        out += int(c[:-1]) * len_route(c, n)
    return out


codes = sys.stdin.readlines()
print("Step 1:", calc_value(codes, 3))
print("Step 2:", calc_value(codes, 26))
