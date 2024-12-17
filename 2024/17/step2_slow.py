import sys


def combo(regs, val):
    if val < 4:
        return val
    return regs[val - 4]


def self_replicate(regs, prog):
    pc = 0
    out = []
    while pc < len(prog):
        ins = prog[pc]
        op = prog[pc + 1]
        # print(pc)
        if ins == 0:  # adv
            regs[0] = regs[0] // (1 << combo(regs, op))
            pc += 2
            continue

        if ins == 1:  # bxl
            regs[1] = regs[1] ^ op
            pc += 2
            continue

        if ins == 2:  # bst
            regs[1] = combo(regs, op) % 8
            pc += 2
            continue

        if ins == 3:  # jnz
            if regs[0] == 0:
                pc += 2
                continue
            pc = op
            continue

        if ins == 4:  # bxc
            regs[1] ^= regs[2]
            pc += 2
            continue

        if ins == 5:  # out
            if len(out) >= len(prog):
                return False
            v = combo(regs, op) & 7
            if v != prog[len(out)]:
                return False
            out.append(v)
            pc += 2
            continue

        if ins == 6:  # bdv
            regs[1] = regs[0] // (1 << combo(regs, op))
            pc += 2
            continue

        if ins == 7:  # cdv
            regs[2] = regs[0] // (1 << combo(regs, op))
            pc += 2
            continue

    return len(out) == len(prog)


regs, prog = sys.stdin.read().split("\n\n")
regs = list(map(lambda x: int(x.split()[-1]), regs.splitlines()))
prog = tuple(map(int, prog.split(": ")[1].split(",")))

n = 0
while True:
    regs = [n, 0, 0]
    if self_replicate(regs, prog):
        print("Step 2:", n)
        break
    n += 1
