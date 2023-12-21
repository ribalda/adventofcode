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


def find_cycle(pos):
    steps = {pos}
    cycle = [set(), set(), set(), set(), start]
    n = 0
    while True:
        n += 1
        squares = calc_out_square(tuple(steps))
        steps = squares[0, 0]
        cycle = cycle[1:] + [steps]
        if cycle[-2] == cycle[-4] and cycle[-3] == cycle[-1]:
            return tuple(cycle[-2:])


def calc_output(pos, cycle_lens, done_squares, out_squares):
    out = 0
    for done in done_squares:
        cycle, idx = done_squares[done]
        idx = (pos - cycle + idx) % 2
        out += cycle_lens[idx]
    out += sum(map(len, out_squares.values()))
    return out


def part2(end):
    cycle = find_cycle(start)
    cycle_lens = [len(x) for x in cycle]

    squares = defaultdict(set)
    done_squares = dict()
    squares[(0, 0)].add(start)

    for idx in range(end):
        out_squares = defaultdict(set)
        for s_in in squares:
            if s_in in done_squares:
                continue
            for a in (-1, 0), (1, 0), (0, -1), (0, 1):
                cmp_sq = (s_in[0] + a[0], s_in[1] + a[1])
                if cmp_sq in done_squares:
                    continue
                if cmp_sq not in squares:
                    break
                if squares[cmp_sq] not in cycle:
                    break
            else:
                if squares[s_in] in cycle:
                    done_squares[s_in] = idx, cycle.index(squares[s_in])
                    continue

            sq = calc_out_square(tuple(squares[s_in]))
            for s in sq:
                border_sq = s_in[0] + s[0], s_in[1] + s[1]
                if border_sq in done_squares:
                    continue
                out_squares[border_sq] |= sq[s]

        for s in set(out_squares.keys()):
            if s in done_squares:
                del out_squares[s]
                continue
        squares = out_squares

    return calc_output(end, cycle_lens, done_squares, out_squares)


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
