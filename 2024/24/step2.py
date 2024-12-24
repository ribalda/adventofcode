import sys
import re


def get_oper_n(ops, oper, i):
    for op in ops:
        a, o, b, c = op
        if o != oper:
            continue
        if a in (f"x{i:02d}", f"y{i:02d}"):
            if b in (f"x{i:02d}", f"y{i:02d}"):
                return op


def find_carry_n(ops, xab, i):
    and_carry = None
    xor_carry = None
    for op in ops:
        a, o, b, c = op
        if o == "AND" and xab in (a, b):
            and_carry = b if xab == a else a
        if o == "XOR" and xab in (a, b):
            xor_carry = b if xab == a else a
    if and_carry != xor_carry:
        print(Error)
    if not (and_carry or xor_carry):
        return None
    return and_carry


def validate_out_carry(ops, i):
    xab = get_oper_n(ops, "XOR", i)
    xab = xab[-1]
    carry = find_carry_n(ops, xab, i)
    if not carry:
        aab = get_oper_n(ops, "AND", i)
        return (xab, aab[-1])

    for op in ops:
        a, o, b, c = op
        if o != "XOR":
            continue
        if set([a, b]) == set([xab, carry]):
            if c[0] != "z":
                return (c, f"z{i:02d}")
    return []


_, init_ops = sys.stdin.read().split("\n\n")


ops = set()
wires = set()
for l in init_ops.splitlines():
    res = re.match(r"(.*) (.*) (.*) -> (.*)", l)
    op = (res.group(1), res.group(2), res.group(3), res.group(4))
    ops.add(op)

out = []
for i in range(1, 45):
    out += validate_out_carry(ops, i)
print("Part 2:", ",".join(sorted(out)))
