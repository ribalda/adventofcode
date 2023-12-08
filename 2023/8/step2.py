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


def lcd(a,b):
    return (a * b) // gcd(a, b)


inst, paths = sys.stdin.read().split("\n\n")

inst = tuple(map(lrtoint, list(inst.strip())))
paths = list(map(lineparse, paths.splitlines()))
road = dict()
for p in paths:
    road[p[0]] = p[1]

out = 1
for r in road:
    if r[-1] == "A":
        offset, cycle = offset_cyle(inst, r)
        if offset != cycle or (offset % len(inst)) !=0:
            print("Can't solve!")
        out = lcd(offset,out)
        
print(out)
