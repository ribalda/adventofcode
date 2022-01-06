import sys


def distance(a, b):
    d = 0
    for i in range(len(a)):
        d += abs(a[i] - b[i])
    return d


def find_max_bot(bots):
    max_r = 0
    max_bot = 0
    for i, bot in enumerate(bots):
        if bot[1] > max_r:
            max_r = bot[1]
            max_bot = i
    return max_bot


def bots_in_range(bots, i):
    r = 1
    for j in range(len(bots)):
        if i == j:
            continue
        if distance(bots[i][0], bots[j][0]) <= bots[i][1]:
            r += 1
    return r


bots = []
lines = sys.stdin.readlines()
for l in lines:
    pos, r = l.strip().split(", ")
    pos = tuple(map(int, pos[5:-1].split(",")))
    r = int(r[2:])
    bots.append((pos, r))

max_bot = find_max_bot(bots)
print(bots_in_range(bots, max_bot))
