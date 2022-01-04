import sys


def convert_line(line):
    line = line.split()
    for i in range(1, 4):
        line[i] = int(line[i])
    return line


def disassemble(lines, i, regs):
    line = lines[i]
    code, a, b, c = line
    print(f"{i}: ", end="")

    if code == "addr":
        print(f"{regs[c]} = {regs[a]} + {regs[b]}")
    elif code == "addi":
        print(f"{regs[c]} = {regs[a]} + {hex(b)}")
    elif code == "mulr":
        print(f"{regs[c]} = {regs[a]} * {regs[b]}")
    elif code == "muli":
        print(f"{regs[c]} = {regs[a]} * {hex(b)}")
    elif code == "banr":
        print(f"{regs[c]} = {regs[a]} & {regs[b]}")
    elif code == "bani":
        print(f"{regs[c]} = {regs[a]} & {hex(b)}")
    elif code == "borr":
        print(f"{regs[c]} = {regs[a]} | {regs[b]}")
    elif code == "bori":
        print(f"{regs[c]} = {regs[a]} | {hex(b)}")
    elif code == "setr":
        print(f"{regs[c]} = {regs[a]}")
    elif code == "seti":
        print(f"{regs[c]} = {hex(a)}")
    elif code == "gtir":
        print(f"{regs[c]} = {hex(a)} > {regs[b]}")
    elif code == "gtri":
        print(f"{regs[c]} = {regs[a]} > {hex(b)}")
    elif code == "gtrr":
        print(f"{regs[c]} = {regs[a]} > {regs[b]}")
    elif code == "eqir":
        print(f"{regs[c]} = {hex(a)} == {regs[b]}")
    elif code == "eqri":
        print(f"{regs[c]} = {regs[a]} == {hex(b)}")
    elif code == "eqrr":
        print(f"{regs[c]} = {regs[a]} == {regs[b]}")
    else:
        print("Error")


lines = sys.stdin.readlines()
ip = int(lines[0].split()[1])
lines = list(map(convert_line, lines[1:]))
regs = ["a", "b", "c", "d", "e", "f"]
regs[ip] = "ip"

for i in range(len(lines)):
    disassemble(lines, i, regs)
