import sys


s = 0

for l in sys.stdin.readlines():
    s += int(l)

print(s)
