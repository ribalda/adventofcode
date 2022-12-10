import sys


def inc_clk(state):
    state["clk"] += 1
    if state["clk"] in {20, 60, 100, 140, 180, 220}:
        state["strength"] += state["clk"] * state["x"]
    return


state = dict()
state["clk"] = 0
state["x"] = 1
state["strength"] = 0

for l in sys.stdin.readlines():
    l = l.split()
    op = l[0]
    if op == "noop":
        inc_clk(state)
    elif op == "addx":
        inc_clk(state)
        inc_clk(state)
        state["x"] += int(l[1])


print(state["strength"])
