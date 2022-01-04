import sys


def create_map(rege):
    mov = {"N": -1, "S": +1, "W": -1j, "E": 1j}
    pos = 0j
    steps = 0
    stack = []
    mapa = dict()
    for r in rege:
        if r == "(":
            stack.append((pos, steps))
            continue
        if r == ")":
            stack.pop()
            continue
        if r == "|":
            pos, steps = stack[-1]
            continue
        pos += mov[r]
        steps += 1
        if pos in mapa:
            steps = min(steps, mapa[pos])
        mapa[pos] = steps
    return mapa


rege = sys.stdin.readline().strip()[1:-1]
mapa = create_map(rege)
print("Step1", max(mapa.values()))
n = len(list(filter(lambda x: x >= 1000, mapa.values())))
print("Step2", n)
