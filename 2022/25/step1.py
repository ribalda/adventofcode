import sys
from functools import cache

SNAFU_ORDER = ("=", "-", "0", "1", "2")
OFFSET = 2

def snafu2int(snaf):
    mult = 1
    out = 0
    for v in reversed(range(len(snaf))):
        out += (SNAFU_ORDER.index(snaf[v]) -OFFSET) * mult
        mult *= len(SNAFU_ORDER)
    return out


def int2snaf(val):
    out = ""
    while val > 0:
        val += OFFSET
        k = val % len(SNAFU_ORDER)
        out = SNAFU_ORDER[k] + out
        val = val // len(SNAFU_ORDER)
    return out


s = 0
for line in sys.stdin.readlines():
    if line[-1] == "\n":
        line = line[:-1]
    v = snafu2int(line)
    s += v

print(int2snaf(s))
