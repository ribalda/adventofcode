import sys
import re
import heapq

MAX_STEP = 26


def calc_potential(visited, step, valves, flow_values):
    out = 0
    for f in flow_values:
        if f in visited:
            continue
        out += (MAX_STEP - step - 1) * valves[f]["rate"]
    return out


def is_todo(visited, state, flow_valves, max_pres):
    _, pot, pres, step, pA, pB, v = state
    if step >= MAX_STEP:
        return False

    if pot <= max_pres:
        return False

    p = str(sorted([pA, pB]))

    if len(v) == len(flow_valves):
        return False

    v = str(sorted(v))

    if p not in visited:
        visited[p] = dict()

    pres = (pres, pot)
    if v not in visited[p]:
        visited[p][v] = pres
        return True

    if visited[p][v] >= pres:
        return False

    visited[p][v] = pres
    return True


flow_valves = set()
valves = dict()
for line in sys.stdin.readlines():
    v = dict()
    m = re.search(
        "Valve (.*) has flow rate=(.*); (?:tunnels lead to valves|tunnel leads to valve) (.*)",
        line,
    )
    name = m.group(1)
    rate = int(m.group(2))
    v["rate"] = rate
    v["tunnels"] = m.group(3).split(", ")
    valves[name] = v
    if rate != 0:
        flow_valves.add(name)

start = (-1, 1, 0, 0, "AA", "AA", set()) # sort, pot, presure, step, posA, posB, open_valves
max_pres = 0
todo = []
heapq.heappush(todo, start)
visited = dict()

while todo:
    _, pot, pres, step, pA, pB, v = heapq.heappop(todo)

    if pot <= max_pres:
        continue

    for pA1 in [pA] + valves[pA]["tunnels"]:
        if pA1 == pA and (pA1 in v or pA1 not in flow_valves):
            continue
        for pB1 in [pB] + valves[pB]["tunnels"]:
            if pB1 == pB and (pB1 in v or pB1 not in flow_valves):
                continue

            if pA1 == pA and pB1 == pB and pA == pB:
                continue

            pres1 = pres
            v1 = v.copy()
            if pA1 == pA:
                pres1 += (MAX_STEP - step - 1) * valves[pA]["rate"]
                v1 |= {pA1}
            if pB1 == pB:
                pres1 += (MAX_STEP - step - 1) * valves[pB]["rate"]
                v1 |= {pB1}

            step1 = step + 1
            pot1 = pres1 + calc_potential(v1, step1, valves, flow_valves)
            state = -pot1, pot1, pres1, step1, pA1, pB1, v1
            if is_todo(visited, state, flow_valves, max_pres):
                heapq.heappush(todo, state)
            else:
                max_pres = max(max_pres, pres1)

print(max_pres)
