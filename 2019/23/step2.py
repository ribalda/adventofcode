import sys
from collections import defaultdict
import copy


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


def run_nic(d):
    d["pc"], d["rel"], ret = execute_prog(
        d["p"], d["pc"], d["rel"], d["inp"], d["outp"])

    if ret == True:
        print("Error")
        1 / 0
    return


def run_nics(nics, nat):
    is_idle = True
    for n in nics:
        if len(n["inp"]) == 0:
            n["inp"] = [-1]
        run_nic(n)
        while(n["outp"]):
            is_idle = False
            dest = n["outp"].pop(0)
            x = n["outp"].pop(0)
            y = n["outp"].pop(0)

            if dest == 255:
                nat[0] = (x, y)
                continue
            nics[dest]["inp"].append(x)
            nics[dest]["inp"].append(y)
    if is_idle and nat[0] != None:
        x, y = nat[0]
        if y == nat[1]:
            print(nat[1])
            return False
        nics[0]["inp"].append(x)
        nics[0]["inp"].append(y)
        nat[1] = y

    return True


line = sys.stdin.readline()
d = parse_prog(line)
nics = []
for i in range(50):
    d2 = copy.deepcopy(d)
    d2["inp"] = [i]
    nics.append(d2)

nat = [None, None]
while run_nics(nics, nat):
    pass
