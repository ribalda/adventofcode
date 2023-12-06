import sys
import math


def calc_winning(t_d):
    out = 0
    t, d = t_d
    for s in range(1, t):
        if (t - s) * s > d:
            out += 1
    return out


times, distances = sys.stdin.readlines()

time = map(int, times.split()[1:])
distance = map(int, distances.split()[1:])

t_d = list(zip(time, distance))
print("Step 1", math.prod(map(calc_winning, t_d)))


time = int("".join(times.split()[1:]))
distance = int("".join(distances.split()[1:]))

print("Step 2", calc_winning((time, distance)))
