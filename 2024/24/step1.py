import sys
import re


def operate(o1, op, o2):
    if op == "XOR":
        return o1 ^ o2
    if op == "AND":
        return o1 & o2
    if op == "OR":
        return o1 | o2
    print(kk)


def solve_all(nodes, ops):
    while True:
        done_ops = set()
        for o in ops:
            if o[0] in nodes and o[2] in nodes:
                nodes[o[3]] = operate(nodes[o[0]], o[1], nodes[o[2]])
                done_ops.add(o)
        if not done_ops:
            break
        ops -= done_ops

    return nodes


def xval(nodes, xval):
    zvalues = reversed(sorted(list(filter(lambda x: x.startswith(xval), nodes))))
    binval = "".join([str(nodes[x]) for x in zvalues])
    return int(binval, 2)


init_vals, init_ops = sys.stdin.read().split("\n\n")

nodes = dict()
for l in init_vals.splitlines():
    name, val = l.split(": ")
    nodes[name] = int(val)

ops = set()
for l in init_ops.splitlines():
    res = re.match(r"(.*) (.*) (.*) -> (.*)", l)
    op = (res.group(1), res.group(2), res.group(3), res.group(4))
    ops.add(op)

print("Step 1:", xval(solve_all(nodes, ops), "z"))
