import sys


def parse_line(l):
    return list(map(int, list(l.strip())))


def sum_nums_idx(lines, idx):
    s_num = 0
    for l in lines:
        s_num += l[idx]
    return s_num


def filter_num(lines, value, pos):
    filtered = []
    for l in lines:
        if l[pos] == value:
            filtered.append(l)
    return filtered


def calculate_gas(lines, inv):
    oxygen = lines[:]    
    for idx in range(len(oxygen[0])):
        s_num = sum_nums_idx(oxygen, idx)
        value = s_num < len(oxygen) / 2
        if inv:
            value = not value
        value = int(value)
        oxygen = filter_num(oxygen, value, idx)
        if len(oxygen) == 1:
            break
    return int("".join([str(int) for int in oxygen[0]]), 2)


lines = sys.stdin.readlines()
lines = list(map(parse_line, lines))

co2 = calculate_gas(lines, True)
oxygen = calculate_gas(lines, False)

print(oxygen * co2)
