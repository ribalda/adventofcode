import sys
import re
from collections import deque

MAX_STEP = 30


def is_todo(visited, state, flow_valves):
    pres, step, p, v = state
    if step >= MAX_STEP:
        return False

    if len(v) == len(flow_valves):
        return False

    v = str(sorted(v))

    if p not in visited:
        visited[p] = dict()

    if v not in visited[p]:
        visited[p][v] = -1

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

start = (0, 0, "AA", set())  # presure, step, location, open_valves
max_pres = -1
todo = deque([start])
visited = dict()

while todo:
    pres, step, p, v = todo.popleft()

    if p not in v and p in flow_valves:
        pres1 = pres + (MAX_STEP - step - 1) * valves[p]["rate"]
        v1 = {p} | v
        state = pres1, step + 1, p, v1
        if is_todo(visited, state, flow_valves):
            todo.append(state)
        else:
            max_pres = max(max_pres, pres)

    for p1 in valves[p]["tunnels"]:
        state = pres, step + 1, p1, v
        if is_todo(visited, state, flow_valves):
            todo.append(state)
        else:
            max_pres = max(max_pres, pres)

print(max_pres)
