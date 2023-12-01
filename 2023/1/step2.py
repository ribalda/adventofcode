import sys
import re


def is_int(ch):
    return ord(ch) in range(ord("0"), ord("9") + 1)


def to_calib(st):
    numbers = "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
    for i, n in enumerate(numbers):
        st = st.replace(n, n + str(i + 1) + n)

    nums = list(map(int, (filter(is_int, list(st)))))
    return nums[0] * 10 + nums[-1]


lines = sys.stdin.readlines()
calibs = map(to_calib, lines)
print(sum(calibs))
