import sys
from collections import deque
import z3


def hash_to_int(target):
    out = 0
    for x in reversed(target):
        out *= 2
        if x == "#":
            out += 1
    return out


def parse_switches(switches):
    switches = map(int, switches[1:-1].split(","))
    return tuple(switches)


def switch2flip(switches):
    out = 0
    for s in switches:
        out += 2**s
    return out


def min_steps1(machine):
    target, switches, _ = machine
    target = hash_to_int(target)
    switches = tuple(map(switch2flip, switches))
    visited = set()
    todo = deque([(0, 0)])
    while todo:
        n, t = todo.popleft()
        if t in visited:
            continue
        visited.add(t)
        if t == target:
            return n
        for s in switches:
            new_t = t ^ s
            todo.append((n + 1, new_t))
    return None


def min_steps2_slow(machine):
    config, switches, target = machine
    visited = set()
    start = tuple([0] * len(config))
    todo = deque([(0, start)])
    while todo:
        n, t = todo.popleft()
        if t in visited:
            continue
        visited.add(t)
        if t == target:
            print(n)
            return n
        for i, x in enumerate(t):
            if x > target[i]:
                continue

        for sw in switches:
            new_t = list(t)
            for s in sw:
                new_t[s] += 1
            todo.append((n + 1, tuple(new_t)))
    return None


def min_steps2(machine):
    config, switches, target = machine

    s = z3.Optimize()
    for i, t in enumerate(target):
        sw_list = list()
        for j, sw in enumerate(switches):
            if i in sw:
                sw_list.append(z3.Int(f"sw{j}"))
        s.add(sum(sw_list) == t)

    sw_list = list()
    for i, sw in enumerate(switches):
        v = z3.Int(f"sw{i}")
        s.add(v >= 0)
        sw_list.append(v)

    num_sw = z3.Int(f"n_sw")
    s.add(sum(sw_list) == num_sw)

    h = s.minimize(num_sw)
    s.check()
    return h.value().as_long()


def parse_line(line):
    target, switches = line.strip()[1:].split("] ")
    switches, jules = switches[:-1].split(" {")
    switches = tuple(map(parse_switches, switches.split(" ")))
    jules = tuple(map(int, jules.split(",")))
    return (target, switches, jules)


machines = tuple(map(parse_line, sys.stdin.readlines()))
print("Part 1:", sum(map(min_steps1, machines)))
print("Part 2:", sum(map(min_steps2, machines)))
