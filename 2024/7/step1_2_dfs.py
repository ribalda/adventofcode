import sys
from collections import deque


def ceil_p10(n):
    out = 10
    while True:
        if n < out:
            return out
        out *= 10


def operate(a, b, op):
    if op == "+":
        return a + b
    elif op == "*":
        return a * b
    elif op == "|":
        return ceil_p10(b) * a + b


def is_valid(target, nums, ops):
    todo = deque([(nums[0], 1)])
    while todo:
        val, pos = todo.popleft()
        for o in ops:
            v = operate(val, nums[pos], o)
            if (pos + 1) == len(nums):
                if v == target:
                    return True
            else:
                todo.appendleft((v, pos + 1))
    return False


out1, out2 = 0, 0
for line in sys.stdin.readlines():
    target, nums = line.split(": ")
    target = int(target)
    nums = tuple(map(int, nums.split()))
    if is_valid(target, nums, ("+", "*")):
        out1 += target
        out2 += target
    elif is_valid(target, nums, ("+", "*", "|")):
        out2 += target
print("Step 1", out1)
print("Step 2", out2)
