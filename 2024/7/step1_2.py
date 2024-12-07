import sys
import itertools


def ceil_p10(n):
    out = 10
    while True:
        if n < out:
            return out
        out *= 10


def is_valid(target, nums, ops):
    for ops in itertools.product(ops, repeat=len(nums) - 1):
        out = nums[0]
        for op, val in zip(ops, nums[1:]):
            if op == "+":
                out += val
            elif op == "*":
                out *= val
            elif op == "|":
                out = ceil_p10(val) * out + val
                # out = int(str(out) + str(val))
            #if out > target: Not true, we could be multiplied by 0 afterwards
            #    break
        if out == target:
            return True

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
