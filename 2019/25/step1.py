import sys
from collections import defaultdict
import copy
import re


def get_arg(mode, arg, p, rel):
    if mode == 0:
        return p[arg]
    elif mode == 1:
        return arg
    elif mode == 2:
        return p[arg + rel]
    else:
        raise NameError(int(mode))


def get_dest(mode, arg, p, rel):
    # print(mode)
    if mode == 0:
        return arg
    elif mode == 2:
        return arg + rel
    else:
        raise NameError(int(mode))


def execute_prog(p, pc, rel, inp, outp):

    while True:
        # print(pc,rel,p[pc],p[pc+1],p[pc+2],p[pc+3])
        # print(outp)
        opcode = p[pc]
        op = opcode % 100
        mode1 = (opcode // 100) % 10
        mode2 = (opcode // 1000) % 10
        mode3 = (opcode // 10000) % 10

        if opcode == 99:
            return [pc, rel, True]

        if op == 1:
            # print("sum")
            arg1 = get_arg(mode1, p[pc + 1], p, rel)
            arg2 = get_arg(mode2, p[pc + 2], p, rel)
            dest = get_dest(mode3, p[pc + 3], p, rel)
            p[dest] = arg1 + arg2
            pc += 4
        elif op == 2:
            # print("mul")
            arg1 = get_arg(mode1, p[pc + 1], p, rel)
            arg2 = get_arg(mode2, p[pc + 2], p, rel)
            dest = get_dest(mode3, p[pc + 3], p, rel)
            p[dest] = arg1 * arg2
            pc += 4
        elif op == 3:
            # print("in")
            if len(inp) < 1:
                return [pc, rel, False]
            dest = get_dest(mode1, p[pc + 1], p, rel)
            p[dest] = inp[0]
            inp.pop(0)
            pc += 2
        elif op == 4:
            # print("out")
            arg1 = get_arg(mode1, p[pc + 1], p, rel)
            outp.append(arg1)
            pc += 2
        elif op == 5:
            # print("jnz", arg1)
            arg1 = get_arg(mode1, p[pc + 1], p, rel)
            arg2 = get_arg(mode2, p[pc + 2], p, rel)
            if arg1 != 0:
                pc = arg2
            else:
                pc += 3
        elif op == 6:
            # print("jz", arg1)
            arg1 = get_arg(mode1, p[pc + 1], p, rel)
            arg2 = get_arg(mode2, p[pc + 2], p, rel)
            if arg1 == 0:
                pc = arg2
            else:
                pc += 3
        elif op == 7:
            # print("cmp less")
            arg1 = get_arg(mode1, p[pc + 1], p, rel)
            arg2 = get_arg(mode2, p[pc + 2], p, rel)
            dest = get_dest(mode3, p[pc + 3], p, rel)
            if arg1 < arg2:
                p[dest] = 1
            else:
                p[dest] = 0
            pc += 4
        elif op == 8:
            # print("cmp eq")
            arg1 = get_arg(mode1, p[pc + 1], p, rel)
            arg2 = get_arg(mode2, p[pc + 2], p, rel)
            dest = get_dest(mode3, p[pc + 3], p, rel)
            if arg1 == arg2:
                p[dest] = 1
            else:
                p[dest] = 0
            pc += 4
        elif op == 9:
            # print("rel +")
            arg1 = get_arg(mode1, p[pc + 1], p, rel)
            rel += arg1
            pc += 2
        else:
            raise NameError(int(op))
        # print()


def parse_prog(line):
    prog_in = list(map(int, line.split(",")))
    prog = defaultdict(int)
    for i in range(len(prog_in)):
        prog[i] = prog_in[i]
    d = dict()
    d["p"] = prog
    d["pc"] = 0
    d["rel"] = 0
    d["inp"] = []
    d["outp"] = []
    return d


def tostr(v):
    if v < 256:
        return chr(v)
    return ""


def run_simu(d, program):
    d = copy.deepcopy(d)
    program = list(program)
    d["inp"] = list(map(ord, program))
    d["pc"], d["rel"], ret = execute_prog(
        d["p"], d["pc"], d["rel"], d["inp"], d["outp"])
    return d, ret


def get_something(lines, something):
    output = []
    for i, l in enumerate(lines):
        if l.startswith(something):
            break
    else:
        return []
    for i in range(i+1, len(lines)):
        line = lines[i].strip()
        if not line.startswith("- "):
            return output
        output.append(line[2:])
    return output


def parse_output(output):
    output = output.split("Command?")
    if output[-1] != "\n":
        print(output[-1])
        return None
    n = -1
    while True:
        n -= 1
        o = output[n]
        o = o.split("\n")
        doors = get_something(o, "Doors here lead:")
        items = get_something(o, "Items here:")
        if len(items) >= 2:
            print(items)
        if doors != [] or items != []:
            return (doors, items)


line = sys.stdin.readline()
d = parse_prog(line)

pos = 0
items = tuple()

orders = dict()
orders[(pos, items)] = ""
todo = [(pos, items)]

while todo:
    t = todo.pop(0)
    print(t)
    pos, items = t
    order = orders[t]
    d2, ret = run_simu(d, order)
    output = "".join(list(map(chr, d2["outp"])))
    if pos.real > 8:
        print(order)
        print(output)
        break
    if ret == True:
        print("Ended")
        print(t)
        print(order)
        print(output)
        sys.exit(0)
        continue
    d_n = parse_output(output)
    if d_n == None:
        print("Error")
        print(t)
        print(order)
        print(output)
        continue
    doors, new_items = d_n
    for i in new_items:
        if i == "infinite loop":
            continue
        if i == "escape pod":
            continue
        if i == "photons":
            continue
        if i == "molten lava":
            continue
        if i == "giant electromagnet":
            continue
        if i in items:
            continue
        items2 = list(items)
        items2.append(i)
        # if len(items2) > 1:
        #    break
        items2 = tuple(sorted(list(items2)))
        pos2 = pos
        if (pos2, items2) in orders:
            continue
        order2 = order + f"take {i}\n"
        orders[(pos2, items2)] = order2
        todo.append((pos2, items2))
    for door in doors:
        items2 = items
        pos2 = pos + {"north": 1, "south": -1, "west": -1j, "east": +1j}[door]
        if (pos2, items2) in orders:
            continue
        order2 = order + f"{door}\n"
        orders[(pos2, items2)] = order2
        todo.append((pos2, items2))
    for i, ite in enumerate(items):
        items2 = items[0:i] + items[i+1:]
        pos2 = pos
        if (pos2, items2) in orders:
            continue
        order2 = order + f"drop {ite}\n"
        orders[(pos2, items2)] = order2
        todo.append((pos2, items2))


#out = run_simu(d, orders)
# print(parse_output(out))
# sys.exit(0)
