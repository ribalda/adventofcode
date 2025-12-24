import sys
import re
import math


def parse1_lines(lines):
    out = []
    for l in lines[:-1]:
        vals = map(int, re.split(r" +", l.strip()))
        out.append(tuple(vals))

    out.append(tuple(re.split(r" +", lines[-1].strip())))
    return out


def part1(lines):
    lines = parse1_lines(lines)
    out = 0
    for i, op in enumerate(lines[-1]):
        if op == "*":
            o = 1
            f = lambda x, y: x * y
        else:
            o = 0
            f = lambda x, y: x + y
        for l in lines[:-1]:
            o = f(o, l[i])
        out += o
    return out


def part2(lines):
    width = len(lines[0].strip())
    out = 0
    last_nums = list()
    for i in range(width, -1, -1):
        try:
            last_nums.append(int("".join([x[i] for x in lines[:-1]])))
        except:
            pass
        op = lines[-1][i]
        if op == " ":
            continue
        if op == "+":
            out += sum(last_nums)
            last_nums = list()
            continue
        if op == "*":
            out += math.prod(last_nums)
            last_nums = list()
            continue
    return out


lines = sys.stdin.readlines()
print("Part 1", part1(lines))
print("Part 2", part2(lines))
