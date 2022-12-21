import sys
from collections import deque

monkeys = dict()

todo = deque([])
for line in sys.stdin.readlines():
    if line[-1] == "\n":
        line = line[:-1]
    name, val = line.split(": ")
    val = val.split(" ")
    if len(val) == 1:
        monkeys[name] = int(val[0])
    else:
        todo.append((name, tuple(val)))

while todo and "root" not in monkeys:
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

print(monkeys["root"])
