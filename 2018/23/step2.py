import sys
import heapq
import z3


def distance(a, b):
    d = 0
    for i in range(len(a)):
        d += abs(a[i] - b[i])
    return d


def bots_in_range(bots, i):
    out = {i}
    for j in range(len(bots)):
        if i == j:
            continue
        if distance(bots[i][0], bots[j][0]) <= (bots[i][1] + bots[j][1]):
            out.add(j)
    # print("range", i, out)
    return out


def zabs(x):
    return z3.If(x >= 0, x, -x)


def best_colision(ranges):
    todo = []
    for i in range(len(ranges)):
        r = sorted(list(ranges[i]))
        r = list(filter(lambda x: x >= i, r))
        heapq.heappush(todo, (-len(r), 0, r))
    best_combos = [[]]
    while todo:
        t = heapq.heappop(todo)
        _, l, combo = t
        if len(combo) < len(best_combos[0]):
            break
        for pos2 in range(l+1, len(combo)):
            combo2 = combo[:l+1] + combo[pos2:]
            combo2 = set(combo2) & ranges[combo[pos2]]
            if len(combo2) < len(best_combos[0]):
                continue
            combo2 = sorted(list(combo2))
            if combo[:l+1] != combo2[:l+1] or combo2[l+1] != combo[pos2]:
                continue
            l2 = l+1
            if l2 == len(combo2) - 1:
                if len(combo2) > len(best_combos[0]):
                    best_combos = []
                else:
                    continue
                best_combos.append(combo2)
                print("found", combo2, len(combo2))
                continue
            heapq.heappush(todo, (-len(combo2), l2, combo2))

    return best_combos


# parse
bots = []
lines = sys.stdin.readlines()
for l in lines:
    pos, r = l.strip().split(", ")
    pos = tuple(map(int, pos[5:-1].split(",")))
    r = int(r[2:])
    bots.append((pos, r))

# find best collision
ranges = []
for i in range(len(bots)):
    ranges.append(bots_in_range(bots, i))
colision = best_colision(ranges)

x = z3.Int('x')
y = z3.Int('y')
z = z3.Int('z')
s = z3.Solver()
for c in colision[0]:
    s.add((zabs(x - bots[c][0][0]) + zabs(y - bots[c][0]
          [1]) + zabs(z - bots[c][0][2])) <= bots[c][1])
s.check()
model = s.model()
print(model)

s = 0
for m in [x, y, z]:
    s += model[m].as_long()
print(s)
