import sys


def is_int(ch):
    return ord(ch) in range(ord("0"), ord("9") + 1)


def to_calib(st):
    nums = list(map(int, (filter(is_int, list(st)))))
    return nums[0] * 10 + nums[-1]


lines = sys.stdin.readlines()
calibs = map(to_calib, lines)
print(sum(calibs))
