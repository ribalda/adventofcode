# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#    | 0 | A |
#    +---+---+

#    +---+---+
#    | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

import sys
from functools import cache


@cache
def paths(a, b):
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
    out_up = out + "A"

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
    out_left = out + "A"

    if pos[a].imag == 0 and pos[b].real == 3:
        return out_left

    if pos[a].real == 3 and pos[b].imag == 0:
        return out_up

    if out_up[-2] in ("^", ">"):
        return out_up
    if out_left[-2] in ("^", ">"):
        return out_left
    if out_up[-2] == "v":
        return out_up
    if out_left[-2] == "v":
        return out_left

    return out_up


def route(st):
    pre = "A"
    out = ""

    for s in st:
        out += paths(pre, s)
        pre = s

    return out


def len_route(st_in, n):
    st = st_in
    for _ in range(n):
        st = route(st)
    return len(st)


def calc_value(codes, n):
    out = 0
    for c in codes:
        c = c.strip()
        out += int(c[:-1]) * len_route(c, n)
        print(c, len_route(c, n))
    return out


codes = sys.stdin.readlines()
print("Step 1:", calc_value(codes, 3))
print("Step 2:", calc_value(codes, 26))
