import sys

lines = sys.stdin.readlines()
sel_nums = 0
for l in lines:
    ten, enabled = l.strip().split(" | ")
    ten = ten.split()
    enabled = enabled.split()
    for e in enabled:
        if len(e) in [2, 4, 3, 7]:
            sel_nums += 1
print(sel_nums)
