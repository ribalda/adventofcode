import sys
from collections import deque


def next_valid_pos(pos, bytes, max_pos):
    for inc in (1j, -1j, 1, -1):
        next_pos = pos + inc
        if pos.real > max_pos or pos.real < 0 or pos.imag > max_pos or pos.imag < 0:
            continue
        if pos in bytes:
            continue
        yield next_pos


def find_path(bytes, max_pos):
    todo = deque([(0, complex(0, 0))])
    visited = set()
    while todo:
        steps, pos = todo.popleft()
        if pos in visited:
            continue
        visited.add(pos)
        for next_pos in next_valid_pos(pos, bytes, max_pos):
            if next_pos == complex(max_pos, max_pos):
                return steps + 1
            todo.append((steps + 1, next_pos))
    return None


def first_blocker(bytes_time, max_pos):
    good = 0
    bad = len(bytes_time) - 1
    while True:
        if bad == good + 1:
            return bytes_time[good]
        test = (bad + good) // 2
        if find_path(set(bytes_time[:test]), max_pos):
            good = test
        else:
            bad = test


if len(sys.argv) > 1:
    max_pos = 6
    sim_time_p1 = 12
else:
    max_pos = 70
    sim_time_p1 = 1024

bytes_time = list()
for line in sys.stdin.readlines():
    a, b = line.split(",")
    byte = complex(int(a), int(b))
    bytes_time.append(byte)

print("Step 1:", find_path(set(bytes_time[0:sim_time_p1]), max_pos))
fb = first_blocker(bytes_time, max_pos)
print(f"Step 2: {int(fb.real)},{int(fb.imag)}")
