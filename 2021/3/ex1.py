import sys


def parse_line(l):
    return list(map(int, list(l.strip())))


lines = sys.stdin.readlines()
n_lines = len(lines)
s_num = parse_line(lines[0])
for l in lines[1:]:
    s_num = [a + b for a, b in zip(s_num, parse_line(l))]

is_even = [str(int(a > (n_lines/2))) for a in s_num]

gamma = int("".join(is_even), 2)
epsilon = gamma ^ ((1 << len(s_num)) - 1)
print(epsilon*gamma)
