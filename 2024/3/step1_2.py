import sys
import re


def calc_value(str):
    pairs = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", str)
    out = 0
    for p in pairs:
        out += int(p[0]) * int(p[1])
    return out


def filter_value(str):
    patterns = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", str)
    out = ""
    valid = True
    for p in patterns:
        if p == "don't()":
            valid = False
            continue
        if p == "do()":
            valid = True
            continue
        if not valid:
            continue
        out += p
    return out


data = "".join(sys.stdin.read())


print("Step 1:", calc_value(data))
print("Step 2:", calc_value(filter_value(data)))
