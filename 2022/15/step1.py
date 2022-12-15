import sys
import re


def dist(a, b):
    d = a - b
    return int(abs(d.real) + abs(d.imag))


def in_range(sensors, p):
    for s in sensors:
        if dist(p, s[0]) <= s[1]:
            return True
    return False


def count_row(sensors, beacons, row):
    left = int(min([x[0].real - x[1] for x in sensors]))
    right = int(max([x[0].real + x[1] for x in sensors]))

    free = 0
    for x in range(left, right + 1):
        p = complex(x, row)
        if p not in beacons and in_range(sensors, p):
            free += 1
    return free


sensors = set()
beacons = set()
for l in sys.stdin.readlines():
    m = re.search("Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)", l)
    sensor = complex(int(m.group(1)), int(m.group(2)))
    beacon = complex(int(m.group(3)), int(m.group(4)))
    beacons.add(beacon)
    sensors.add((sensor, dist(sensor, beacon)))


print("Input", count_row(sensors, beacons, 2000000))
print("Example", count_row(sensors, beacons, 10))
