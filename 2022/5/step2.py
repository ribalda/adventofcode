import sys

input = sys.stdin.read()

initial, movements = input.split("\n\n")

stacks = dict()
for l in initial.splitlines()[:-1]:
    for i in range(1, len(l), 4):
        val = l[i]
        if val == " ":
            continue
        idx = (i // 4) + 1
        if idx not in stacks:
            stacks[idx] = []
        stacks[idx].insert(0, val)

for move in movements.splitlines():
    _, n, _, start, _, end = move.split()
    n = int(n)
    start = int(start)
    end = int(end)
    vals = stacks[start][-n:]
    stacks[start] = stacks[start][:-n]
    stacks[end] += vals

i = 1
out = ""
while i in stacks:
    out += stacks[i][-1]
    i += 1
print(out)
# print(initial)
