import sys
from collections import defaultdict
import copy
import itertools


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


def run_simu(d, program):
    d = copy.deepcopy(d)
    program = list(program)
    d["inp"] = list(map(ord,program))
    _, _, ret = execute_prog(d["p"], d["pc"], d["rel"], d["inp"], d["outp"])
    if ret == False:
        print("Error")
        1 / 0

    out = d["outp"]
    if out[-1] > 256:
        return str(out[-1])
    return "".join(list(map(chr,out)))



line = sys.stdin.readline()
d = parse_prog(line)


v = True, False, None
for combo in itertools.product(v,v,v,v,v,v,v,v,v,["A","B","C","D","E","F","G","H","I", None]):
    #prog = ""
    prog = "NOT J J\n"
    for i,v in enumerate(["A","B","C","D","E","F","G","H","I"]):
        if combo[i] == None: 
            continue
        if combo[i]:
            prog += f"AND {v} J\n" 
            continue
        prog += f"NOT {v} T\n" 
        prog += f"AND T J\n" 
    
    if combo[-1] != None:
        prog += f"NOT {combo[-1]} T\n"
        prog += f"OR T J\n" 
    prog += "RUN\n"
    if len(prog.splitlines()) > 16:
        continue
    out = run_simu(d, prog)
    #print(out)
    if "Didn't make it across" not in out:
        print(prog)
        print(out)
        break