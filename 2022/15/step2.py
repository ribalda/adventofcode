import sys
import re
import z3

MAX = 4000000


def dist(a, b):
    d = a - b
    return int(abs(d.real) + abs(d.imag))


def in_range(sensors, p):
    for s in sensors:
        if dist(p, s[0]) <= s[1]:
            return True
    return False


def slow_solver(sensors, maxv):
    for x in range(maxv + 1):
        for y in range(maxv + 1):
            p = complex(x, y)
            if not in_range(sensors, p):
                print(p)
                print(int(p.real * 4000000 + p.imag))
                break


sensors = set()
beacons = set()
for l in sys.stdin.readlines():
    m = re.search("Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", l)
    sensor = complex(int(m.group(1)), int(m.group(2)))
    beacon = complex(int(m.group(3)), int(m.group(4)))
    beacons.add(beacon)
    sensors.add((sensor, dist(sensor, beacon)))


def zabs(k):
    return z3.If(k >= 0, k, -k)


x = z3.Int("x")
y = z3.Int("y")
solv = z3.Solver()
solv.add(x <= MAX)
solv.add(y <= MAX)
solv.add(x >= 0)
solv.add(y >= 0)
for s in sensors:
    solv.add((zabs(x - int(s[0].real)) + zabs(y - int(s[0].imag))) > s[1])
solv.check()
model = solv.model()
print(model)
print(model[x].as_long() * 4000000 + model[y].as_long())

slow_solver(sensors, MAX)
