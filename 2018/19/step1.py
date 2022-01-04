import sys


def convert_line(line):
    line = line.split()
    for i in range(1, 4):
        line[i] = int(line[i])
    return line


def step(lines, regs, ip):
    if regs[ip] >= len(lines) or regs[ip] < 0:
        return False
    code, a, b, c = lines[regs[ip]]

    if code == "addr":
        regs[c] = regs[a] + regs[b]
    elif code == "addi":
        regs[c] = regs[a] + b
    elif code == "mulr":
        regs[c] = regs[a] * regs[b]
    elif code == "muli":
        regs[c] = regs[a] * b
    elif code == "banr":
        regs[c] = regs[a] & regs[b]
    elif code == "bani":
        regs[c] = regs[a] & b
    elif code == "borr":
        regs[c] = regs[a] | regs[b]
    elif code == "bori":
        regs[c] = regs[a] | b
    elif code == "setr":
        regs[c] = regs[a]
    elif code == "seti":
        regs[c] = a
    elif code == "gtir":
        regs[c] = int(a > regs[b])
    elif code == "gtri":
        regs[c] = int(regs[a] > b)
    elif code == "gtrr":
        regs[c] = int(regs[a] > regs[b])
    elif code == "eqir":
        regs[c] = int(a == regs[b])
    elif code == "eqri":
        regs[c] = int(regs[a] == b)
    elif code == "eqrr":
        regs[c] = int(regs[a] == regs[b])
    else:
        print("Error")
        return False

    regs[ip] += 1
    return True


lines = sys.stdin.readlines()
ip = int(lines[0].split()[1])
lines = list(map(convert_line, lines[1:]))
regs = [0] * 6

while step(lines, regs, ip):
    pass
print(regs)
