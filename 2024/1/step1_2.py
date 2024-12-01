import sys

left, right = [], []
for line in sys.stdin.readlines():
    a, b = map(int, line.split())
    left.append(a)
    right.append(b)
left.sort()
right.sort()

# step 1
out = 0
for x in zip(left, right):
    out += abs(x[0] - x[1])

print("Step 1:", out)

# Step 2
from collections import Counter

out = 0
right = Counter(right)
for x in left:
    out += x * right[x]

print("Step 2:", out)
