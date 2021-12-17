import sys
import math


def get_min_v0(x0):
    sol = (math.sqrt(1 + 8 * x0) - 1) / 2
    return math.ceil(sol)


def calc_speed(t, s):
    sol = 2 * s + t * t - t
    return sol / (2 * t)


def calc_time(s, v):
    sol = -8 * s + 4 * v * v + 4 * v + 1
    if sol < 0:
        return None

    sol1 = math.sqrt(sol) + 2 * v + 1
    sol2 = -math.sqrt(sol) + 2 * v + 1
    return sorted([sol1 / 2, sol2 / 2])


line = sys.stdin.readline().strip()
_, _, x, y = line.split()
x = list(map(int, x[2:-1].split("..")))
y = list(map(int, y[2:].split("..")))

max_v0_x = x[1] + 1
min_v0_x = get_min_v0(x[0])

valid_t = set()
for i in range(min_v0_x, max_v0_x + 1):
    cros_x0 = calc_time(x[0], i)
    if cros_x0 == None:
        continue
    cros_x1 = calc_time(x[1], i)
    if cros_x1 == None:
        times = range(
            math.ceil(cros_x0[0]), math.ceil(cros_x0[0]) + 1000
        )  # +1000 is a hack
    else:
        times = range(math.ceil(cros_x0[0]), math.floor(cros_x1[0]) + 1)
    valid_t |= set(times)
valid_v = set()
for t in valid_t:
    valid_v |= set(
        range(math.ceil(calc_speed(t, y[0])), math.floor(calc_speed(t, y[1])) + 1)
    )

max_v = max(valid_v)
print(max_v * (max_v + 1) // 2)
