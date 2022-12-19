import sys
import re
import heapq
from functools import cache

ELEMENTS = ("ore", "clay", "obsidian", "geode")
MAX_MINUTE = 32


def produce_all_robots(blue, elements, robots):
    out = list()
    out.append(((tuple(elements), tuple(robots))))
    for enable in range(len(elements)):
        elements1 = list(elements)
        robots1 = list(robots)
        for j in range(len(elements)):
            elements1[j] -= blue[enable][j]
            if elements1[j] < 0:
                break
        else:
            robots1[enable] += 1
            out.append(((tuple(elements1), tuple(robots1))))
    return out


def produce_elements(elements, robots):
    out = list(elements)
    for i, n in enumerate(robots):
        out[i] += n
    return tuple(out)


@cache
def calc_hyp_max(minute, r, e):
    out = e
    for minute in range(minute, MAX_MINUTE + 1):
        out += r
        r += 1

    return out


def find_max_geode(blue):
    e = tuple([0] * len(ELEMENTS))
    r = tuple([1] + [0] * (len(ELEMENTS) - 1))
    state0 = (0, 0, e, r)
    todo = []
    heapq.heappush(todo, state0)
    max_geode = 0
    v = (e, r)
    visited = dict()
    visited[v] = True
    while todo:
        _, minute, elements, robots = heapq.heappop(todo)

        # inc minute
        minute += 1

        # No dot produce robots on last cycle
        if minute == MAX_MINUTE:
            e = produce_elements(elements, robots)
            return e[-1]

        for t in produce_all_robots(blue, elements, list(robots)):
            e, r = t
            e = produce_elements(e, robots)
            geode = e[-1]
            max_geode = max(max_geode, geode)
            hyp_max = calc_hyp_max(minute, r[-1], e[-1])
            if hyp_max <= max_geode:
                continue
            v = (e, r)
            if v not in visited:
                visited[v] = True
                t1 = (-hyp_max, minute, e, r)
                heapq.heappush(todo, t1)

    print(max_geode)
    return max_geode


blueprints = []
for i, line in enumerate(sys.stdin.readlines()):
    robot_cost = []
    m = re.search("Blueprint (\d+): (.*)", line)
    if int(m.group(1)) != i + 1:
        print("Error")
    costs = m.group(2)[:-1]
    for r, robot in enumerate(costs.split(". ")):
        m = re.search("Each (.+) robot costs (.*)", robot)
        if ELEMENTS.index(m.group(1)) != r:
            print("Error 1")
        costs = [0] * len(ELEMENTS)
        for cost in m.group(2).split(" and "):
            n, ele = cost.split()
            costs[ELEMENTS.index(ele)] = int(n)
        robot_cost.append(tuple(costs))
    blueprints.append(tuple(robot_cost))

quality = 1
for idx, b in enumerate(blueprints[:3]):
    max_g = find_max_geode(b)
    print("Blueprint:", idx + 1, "Max_geodes:", max_g)
    quality *= max_g

print("Quality:", quality)
