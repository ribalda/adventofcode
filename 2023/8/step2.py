import sys
from math import gcd


def lrtoint(lr):
    conv = {"L": 0, "R": 1}
    return conv[lr]


def lineparse(line):
    fr, to = line.split(" = ")
    to = to[1:-1].split(", ")
    return fr, tuple(to)


def offset_cyle(inst, pos):
    steps = 0
    offset = None
    while pos[-1] != "Z" or not offset:
        if pos[-1] == "Z":
            offset = steps
        pos = road[pos][inst[steps % len(inst)]]
        steps += 1
    cycle = steps - offset
    return offset, cycle


def merge_oc_simple(ocs):
    a = ocs[0][0]
    b = ocs[1][0]
    mcm = (a * b) // gcd(a, b)
    return mcm, mcm


def merge_oc(ocs):
    if ocs[0][0] == ocs[0][1] and ocs[1][0] == ocs[1][1]:
        return merge_oc_simple(ocs)
    offset_out = None
    visited = dict()
    while True:
        for idx, (offset, cycle) in enumerate(ocs):
            v = visited.pop(offset, 0)
            v += 1
            visited[offset] = v
            if v == len(offset_cycles):
                if offset_out == None:
                    offset_out = offset
                else:
                    return offset_out, offset - offset_out
            offset += cycle
            ocs[idx] = (offset, cycle)


inst, paths = sys.stdin.read().split("\n\n")

inst = tuple(map(lrtoint, list(inst.strip())))
paths = list(map(lineparse, paths.splitlines()))
road = dict()
for p in paths:
    road[p[0]] = p[1]

offset_cycles = dict()
for r in road:
    if r[-1] == "A":
        offset_cycles[r] = offset_cyle(inst, r)

visited = dict()

offset_cycles = list(offset_cycles.values())
merged = offset_cycles[0]

for o_c in offset_cycles[1:]:
    merged = merge_oc([merged, o_c])

print(merged[0])
