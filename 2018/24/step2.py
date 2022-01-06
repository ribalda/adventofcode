import enum
import sys
import re
import copy


def match_unit(line, team, n):
    unit = dict()
    unit["team"] = team
    unit["n"] = n
    m = re.search(r"(.*) units each", line)
    unit["count"] = int(m.group(1))
    m = re.search(r"with (.*) hit points", line)
    unit["health"] = int(m.group(1))
    m = re.search(r"with an attack that does (.*) (.*) damage", line)
    unit["attack"] = int(m.group(1))
    unit["weapon"] = m.group(2)
    unit["immune"] = []
    unit["weak"] = []
    m = re.search(r"points \((.*)\) with", line)
    if m != None:
        prop = m.group(1)
        for p in prop.split("; "):
            m = re.search(r"(immune|weak) to (.*)", p)
            unit[m.group(1)] = m.group(2).split(", ")
    m = re.search(r"at initiative (.*)", line)
    unit["initiative"] = int(m.group(1))
    return unit


def choose_target(units):
    order = []
    for i, u in enumerate(units):
        order.append((u["count"] * u["attack"], u["initiative"], i))
        u["attacker"] = None
    order.sort(reverse=True)
    # print(order)
    for o in order:
        i = o[-1]
        attack = units[i]
        if attack["count"] <= 0:
            continue
        best_team = None
        for j, defend in enumerate(units):
            if (
                defend["count"] <= 0
                or defend["team"] == attack["team"]
                or defend["attacker"] != None
            ):
                continue
            if attack["weapon"] in defend["immune"]:
                continue
            if attack["weapon"] in defend["weak"]:
                pow = 2
            else:
                pow = 1
            t = (pow, defend["count"] * defend["attack"], defend["initiative"], j)
            if best_team == None:
                best_team = t
            else:
                best_team = max(t, best_team)
        if best_team == None:
            attack["target"] = None
        else:
            attack["target"] = best_team[-1]
            units[best_team[-1]]["attacker"] = i


def attack(units):
    order = []
    for i, u in enumerate(units):
        order.append((u["initiative"], i))
    order.sort(reverse=True)
    # print(order)
    for o in order:
        i = o[-1]
        attack = units[i]
        if attack["count"] <= 0:
            continue
        if attack["target"] == None:
            continue
        target = units[attack["target"]]
        pow = attack["count"] * attack["attack"]
        if attack["weapon"] in target["weak"]:
            pow *= 2
        units_lost = pow // target["health"]
        target["count"] -= units_lost
        target["count"] = max(0, target["count"])


def step(units):
    counts = dict()
    for u in units:
        if u["team"] not in counts:
            counts[u["team"]] = 0
        counts[u["team"]] += u["count"]
    if 0 in counts.values():
        return counts

    choose_target(units)
    attack(units)
    return None


def debug(units):
    print()
    for u in units:
        print(u["team"], u["n"], ":", u["count"])


def play(units_in):
    units = copy.deepcopy(units_in)
    while True:
        counts = step(units)
        if counts != None:
            break
    return counts


def boost(units, n):
    for u in units:
        if u["team"] != "Infection":
            u["attack"] += n


lines = sys.stdin.readlines()
team = None
units = []
n = 0
for l in lines:
    l = l.strip()
    if l == "":
        continue
    if l in ["Immune System:", "Infection:"]:
        team = l[:-1]
        n = 1
        continue
    unit = match_unit(l, team, n)
    units.append(unit)
    n += 1

n = 0
while True:
    boost(units, n)
    c = play(units)
    print(n, c)
    if c["Infection"] == 0:
        print(sum(c.values()))
        break
    n += 1
