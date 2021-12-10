import sys


def calc_err(line):
    table = {"(": [0, 1], ")": [0, -1], "[": [1, 1],  "]": [1, -1],
             "{": [2, 1], "}": [2, -1], "<": [3, 1], ">": [3, -1], }
    stack = []
    points = [3, 57, 1197, 25137]

    for l in line:
        idx, val = table[l]
        if val > 0:
            stack.append(idx)
        elif val < 0:
            if stack[-1] == idx:
                stack = stack[:-1]
            else:
                return points[idx]
    return 0


lines = sys.stdin.readlines()

points = 0
for l in lines:
    points += calc_err(l.strip())

print(points)
