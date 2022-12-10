import sys


def inc_clk(state):
    L = 40
    state["clk"] += 1
    xpos = (state["clk"] - 1) % L
    if abs(state["x"] - xpos) < 2:
        print("#", end="")
    else:
        print(" ", end="")
    if xpos == L - 1:
        print()

    return


state = dict()
state["clk"] = 0
state["x"] = 1

for l in sys.stdin.readlines():
    l = l.split()
    op = l[0]
    if op == "noop":
        inc_clk(state)
    elif op == "addx":
        inc_clk(state)
        inc_clk(state)
        state["x"] += int(l[1])
