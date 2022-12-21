import sys
from collections import deque

monkeys = dict()
monkeys["monkeyzero"] = 0

todo = deque([])
for line in sys.stdin.readlines():
    if line[-1] == "\n":
        line = line[:-1]
    name, val = line.split(": ")
    val = val.split(" ")
    if name == "humn":
        continue
    if len(val) == 1:
        monkeys[name] = int(val[0])
        continue

    m1, op, m2 = val
    if name == "root":
        todo.append((m1, (m2, "+", "monkeyzero")))
        todo.append((m2, (m1, "+", "monkeyzero")))
        continue

    a, b, c = name, m1, m2
    todo.append((name, tuple(val)))
    if op == "+":
        todo.append((b, (a, "-", c)))
        todo.append((c, (a, "-", b)))
    elif op == "-":
        todo.append((b, (a, "+", c)))
        todo.append((c, (b, "-", a)))
    elif op == "*":
        todo.append((b, (a, "/", c)))
        todo.append((c, (a, "/", b)))
    elif op == "/":
        todo.append((b, (a, "*", c)))
        todo.append((c, (b, "/", a)))

while todo and "humn" not in monkeys:
    t = todo.popleft()
    name, (m1, op, m2) = t
    if not (m1 in monkeys and m2 in monkeys):
        todo.append(t)
        continue

    v1 = monkeys[m1]
    v2 = monkeys[m2]

    if op == "+":
        out = v1 + v2
    elif op == "-":
        out = v1 - v2
    elif op == "*":
        out = v1 * v2
    elif op == "/":
        out = v1 // v2
    monkeys[name] = out

print(monkeys["humn"])
