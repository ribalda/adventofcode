import sys


def get_incomplete(line):
    table = {"(": [0, 1], ")": [0, -1], "[": [1, 1],  "]": [1, -1],
             "{": [2, 1], "}": [2, -1], "<": [3, 1], ">": [3, -1], }
    stack = []

    for l in line:
        idx, val = table[l]
        if val > 0:
            stack.append(idx)
        elif val < 0:
            if stack[-1] == idx:
                stack = stack[:-1]
            else:
                # err
                return None
    return stack


def calc_points(stack):
    values = [1, 2, 3, 4]

    out = 0
    for p in reversed(stack):
        out *= 5
        out += values[p]
    return out


lines = sys.stdin.readlines()

values = []
for l in lines:
    stack = get_incomplete(l.strip())
    if not stack:
        continue
    values.append(calc_points(stack))

values.sort()
print(values[len(values)//2])
