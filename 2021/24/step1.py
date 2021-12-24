import sys
from collections import deque


def value(vars, a):
    if isinstance(a, int):
        return a
    return vars[a]


estates = set()


def simulate(lines, vars):
    if vars in estates:
        return None
    estates.add(vars)
    vars = tuple2vars(vars)
    while vars["index"] < len(lines):
        l = lines[vars["index"]]
        vars["index"] += 1
        if l[0] == "inp":
            out = []
            for i in range(1, 10):
                v2 = vars.copy()
                v2[l[1]] = i
                out.append(vars2tuple(v2))
            return out
        if l[0] == "add":
            vars[l[1]] += value(vars, l[2])
        elif l[0] == "mul":
            vars[l[1]] *= value(vars, l[2])
        elif l[0] == "div":
            v = value(vars, l[2])
            if v == 0:
                return None
            vars[l[1]] //= v
        elif l[0] == "mod":
            v = value(vars, l[2])
            if v == 0:
                return None
            vars[l[1]] %= v
        elif l[0] == "eql":
            vars[l[1]] = int(vars[l[1]] == value(vars, l[2]))
        else:
            print("error", l)
    return [vars2tuple(vars)]


def vars2tuple(vars):
    return (vars["w"], vars["x"], vars["y"], vars["z"], vars["index"])


def tuple2vars(t):
    return {"w": t[0], "x": t[1], "y": t[2], "z": t[3], "index": t[4]}


def conv_lines(l):
    l = l.split()
    for i in range(2, len(l)):
        if l[i] in ["w", "x", "y", "z"]:
            continue
        l[i] = int(l[i])
    return l


lines = sys.stdin.readlines()
lines = list(map(conv_lines, lines))
vars = (0, 0, 0, 0, 0)
todo = deque()
todo.append((0, vars))
result = 0
while todo:
    n, v = todo.pop()
    out = simulate(lines, v)
    if out == None:
        continue
    if len(out) == 1:
        if n % 100000000 == 99999999:
            print(n, v, len(estates), len(todo))
            if len(estates) > 1000000:
                print("FLUSH")
                estates = set()
        vars = tuple2vars(out[0])
        if vars["z"] == 0:
            print(n)
            break
        continue
    for i, v2 in enumerate(out):
        r = n * 10 + (i + 1)
        todo.append((r, v2))
