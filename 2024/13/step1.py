import sys
import re
from z3 import Int, Optimize, unsat


def n_tokens(machine, offset):
    a = Int("A")
    b = Int("B")
    cost = Int("cost")
    opt = Optimize()

    opt.add(a * machine[0][0] + b * machine[1][0] == machine[2][0] + offset)
    opt.add(a * machine[0][1] + b * machine[1][1] == machine[2][1] + offset)
    if offset == 0:
        opt.add(a <= 100, b <= 100)
    opt.add(a >= 0, b >= 0)
    opt.add(cost == 3 * a + b)
    h = opt.minimize(cost)
    if opt.check() == unsat:
        return 0
    return opt.lower(h).as_long()


def match_pair(pair):
    regex = r".*X.(.*),.*Y.(.*)"
    m = re.match(regex, pair)
    return (int(m.group(1)), int(m.group(2)))


def parse_machine(machine):
    return tuple(map(match_pair, machine.splitlines()))


machines = list(map(parse_machine, sys.stdin.read().split("\n\n")))
print("Part 1:", sum(map(lambda x: n_tokens(x, 0), machines)))
print("Part 2:", sum(map(lambda x: n_tokens(x, 10000000000000), machines)))
