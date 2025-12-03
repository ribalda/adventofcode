import sys


def get_battery(line):
    return tuple(map(int, line.strip()))


def calc_jolt(battery, n):
    out = 0
    pos = 0
    total_len = len(battery)
    for last in range(total_len - n + 1, total_len + 1):
        v = max(battery[pos:last])
        pos = battery.index(v, pos) + 1
        out = out * 10 + v
    return out


batteries = tuple(map(get_battery, sys.stdin.readlines()))

print("Part 1:", sum(map(lambda x: calc_jolt(x, 2), batteries)))
print("Part 2:", sum(map(lambda x: calc_jolt(x, 12), batteries)))
