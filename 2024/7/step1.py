import sys


def is_valid(target, nums):
    n_ops = len(nums) - 1
    for i in range(1 << n_ops):
        out = nums[0]
        for j in range(n_ops):
            if i & (1 << j):
                out += nums[j + 1]
            else:
                out *= nums[j + 1]
            if out > target:
                break
        if out == target:
            return True

    return False


out = 0
for line in sys.stdin.readlines():
    target, nums = line.split(": ")
    target = int(target)
    nums = list(map(int, nums.split()))
    if is_valid(target, nums):
        out += target
print(out)
