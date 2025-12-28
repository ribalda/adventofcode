import sys
from collections import deque
from functools import cache


def parse_links(lines):
    out = dict()
    for l in lines:
        fr, tos = l.strip().split(": ")
        tos = tos.split(" ")
        out[fr] = set(tos)
    return out


def part1(links):
    todo = deque(["you"])
    out = 0
    while todo:
        t = todo.popleft()
        if t == "out":
            out += 1
            continue
        for next in links.get(t, set()):
            todo.append(next)
    return out


def part2_slow(links):
    todo = deque([["svr"]])
    out = 0
    while todo:
        path = todo.popleft()
        last = path[-1]
        if last == "out":
            if "fft" in path and "dac" in path:
                out += 1
            continue
        for next in links.get(last, set()):
            todo.append(path + [next])
    return out


@cache
def part2(fr, to):

    if fr == to:
        return 1

    out = 0
    for next in links.get(fr, set()):
        out += part2(next, to)
    return out


links = parse_links(sys.stdin.readlines())
print("Part 1:", part1(links))
print("Part 2:", part2("svr", "fft") * part2("fft", "dac") * part2("dac", "out"))
