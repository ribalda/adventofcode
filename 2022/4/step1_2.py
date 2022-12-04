import sys


def is_included(a, b):
    if a[0] >= b[0] and a[1] <= b[1]:
        return True
    return False


def overlap(a, b):
    if a[1] >= b[0] and a[1] <= b[1]:
        return True
    return False


def to_nums(t):
    return list(map(int, t.split("-")))


ret1 = 0
ret2 = 0
for l in sys.stdin.readlines():
    left, right = l.split(",")
    left = to_nums(left)
    right = to_nums(right)
    if is_included(left, right) or is_included(right, left):
        ret1 += 1
    if overlap(left, right) or overlap(right, left):
        ret2 += 1

print("Step1:", ret1, "Step2:", ret2)
