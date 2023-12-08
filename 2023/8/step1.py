import sys


def lrtoint(lr):
    conv = {"L": 0, "R": 1}
    return conv[lr]


def lineparse(line):
    fr, to = line.split(" = ")
    to = to[1:-1].split(", ")
    return fr, tuple(to)


inst, paths = sys.stdin.read().split("\n\n")

inst = tuple(map(lrtoint, list(inst.strip())))
paths = list(map(lineparse, paths.splitlines()))
road = dict()
for p in paths:
    road[p[0]] = p[1]

pos = "AAA"
steps = 0
while pos != "ZZZ":
    pos = road[pos][inst[steps % len(inst)]]
    steps += 1

print(steps)
