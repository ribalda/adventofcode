import sys
from collections import deque


def combo(regs, val):
    if val < 4:
        return val
    return regs[val - 4]


def execute(regs, prog):
    pc = 0
    out = []
    while pc < len(prog):
        ins = prog[pc]
        op = prog[pc + 1]
        if ins == 0:  # adv
            regs[0] >>= combo(regs, op)
        elif ins == 1:  # bxl
            regs[1] ^= op
        elif ins == 2:  # bst
            regs[1] = combo(regs, op) & 7
        elif ins == 3:  # jnz
            if regs[0]:
                pc = op
                continue
        elif ins == 4:  # bxc
            regs[1] ^= regs[2]
        elif ins == 5:  # out
            out.append(combo(regs, op) & 7)
        elif ins == 6:  # bdv
            regs[1] = regs[0] >> combo(regs, op)
        elif ins == 7:  # cdv
            regs[2] = regs[0] >> combo(regs, op)
        pc += 2

    return out


def valid_triple(prog, regA, n_triple):
    inc = 2 ** (n_triple * 3)
    regA -= inc
    valid_tri = []
    for _ in range(8):
        regA += inc
        regs = [regA, 0, 0]
        out = execute(regs, prog)
        if len(out) != len(prog):
            continue
        if prog[n_triple] == out[n_triple]:
            valid_tri.append(regA)
    return valid_tri


def find_self_prog(prog):
    todo = deque([(0, len(prog) - 1)])
    while todo:
        regA, n_triple = todo.popleft()
        for regA in valid_triple(prog, regA, n_triple):
            if n_triple == 0:
                return regA
            todo.append((regA, n_triple - 1))


regs, prog = sys.stdin.read().split("\n\n")
regs = list(map(lambda x: int(x.split()[-1]), regs.splitlines()))
prog = tuple(map(int, prog.split(": ")[1].split(",")))

print("Step 1:", ",".join(map(str, execute(regs, prog))))
print("Step 2:", find_self_prog(prog))
