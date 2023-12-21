import sys
from functools import lru_cache
from collections import defaultdict


def calc_out(steps):
    steps_out = set()
    for s in steps:
        steps_out.add((s[0], s[1] + 1))
        steps_out.add((s[0], s[1] - 1))
        steps_out.add((s[0] + 1, s[1]))
        steps_out.add((s[0] - 1, s[1]))
    return steps_out - rocks


def extend_rocks_part2(rocks):
    rocks = rocks.copy()
    for l in range(nlines):
        if (l, ncols - 1) in rocks:
            rocks.add((l, -1))
        if (l, 0) in rocks:
            rocks.add((l, ncols))
    for c in range(ncols):
        if (nlines - 1, c) in rocks:
            rocks.add((-1, c))
        if (0, c) in rocks:
            rocks.add((nlines, c))
    return rocks


def calc_borders(steps):
    squares = defaultdict(set)
    squares[(0, 0)] = set()
    for move in steps:
        if move[0] < 0:
            squares[-1, 0].add((nlines - 1, move[1]))
            continue
        if move[0] == nlines:
            squares[1, 0].add((0, move[1]))
            continue
        if move[1] < 0:
            squares[0, -1].add((move[0], ncols - 1))
            continue
        if move[1] == ncols:
            squares[0, 1].add((move[0], 0))
            continue
        squares[0, 0].add(move)
    return squares


@lru_cache(maxsize=None)
def calc_out_square(steps):
    steps = calc_out(set(steps))
    return calc_borders(steps)


def part2(end_in):
    squares = defaultdict(set)
    squares[(0, 0)].add(start)
    st = ncols // 2
    end = st + 2 * ncols
    if end >= end_in:
        end = end_in
    if end_in % ncols != st and end_in > end:
        print("cannot solve")
        return
    if ncols != nlines:
        print("cannot solve")
        return
    for idx in range(end):
        out_squares = defaultdict(set)
        for s_in in squares:
            sq = calc_out_square(tuple(squares[s_in]))
            for s in sq:
                out_squares[s_in[0] + s[0], s_in[1] + s[1]] |= sq[s]
        squares = out_squares
        i = idx + 1
        if i % ncols == st:
            print(i, sum(map(len, squares.values())))

    if idx == end_in - 1:
        return sum(map(len, squares.values()))

    return (
        "Use wolphram alpha to fit a cuadratic with the given numbers and then solve for "
        + str(end_in // ncols)
    )


if len(sys.argv) == 1:
    end = 26501365
else:
    end = int(sys.argv[1])

lines_in = sys.stdin.readlines()

rocks_in = set()
for idx, line in enumerate(lines_in):
    for jdx, v in enumerate(line.strip()):
        pos = (idx, jdx)
        if v == "S":
            start = pos
        if v == "#":
            rocks_in.add(pos)

nlines = len(lines_in)
ncols = len(lines_in[0].strip())

rocks = extend_rocks_part2(rocks_in)
print("Step 2:", part2(end))
