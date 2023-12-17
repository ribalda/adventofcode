import sys
import heapq


def next_dirs(dir, run, max_run, min_run):
    if dir != 0 and run < max_run:
        yield dir
    if run < min_run and dir != 0:
        return
    if dir.real == 0:
        for i in -1, 1:
            yield complex(i, 0)
    if dir.imag == 0:
        for i in -1, 1:
            yield complex(0, i)


def count_steps(mapa, max_run, min_run):
    todo = []
    steps = -mapa[complex(0, 0)]
    pos = complex(0, 0)
    dir = complex(0, 0)
    run = 0
    dummy = 0
    heapq.heappush(todo, (steps, dummy, pos, dir, run, complex(0, 0)))
    visited = {}

    while todo:
        steps, _, pos, dir, run, fr = heapq.heappop(todo)

        if pos == end and run > min_run - 1:
            steps += mapa[pos]
            return steps

        visited_idx = pos, dir, run
        if visited_idx in visited:
            if steps >= visited[visited_idx]:
                continue
        visited[visited_idx] = steps

        next_steps = steps + mapa[pos]
        for next_dir in next_dirs(dir, run, max_run, min_run):
            next_run = run
            if dir == next_dir:
                next_run = run + 1
            else:
                next_run = 1
            next_pos = pos + next_dir
            if next_pos not in mapa:
                continue
            dummy += 1
            t = next_steps, dummy, next_pos, next_dir, next_run, pos
            heapq.heappush(todo, t)
    return None


lines = sys.stdin.readlines()

mapa = {}
for idx, line in enumerate(lines):
    for jdx, val in enumerate(line.strip()):
        mapa[complex(idx, jdx)] = int(val)
end = complex(len(lines) - 1, len(lines[0].strip()) - 1)
print("Step 1:", count_steps(mapa, 3, 1))
print("Step 2:", count_steps(mapa, 10, 4))
