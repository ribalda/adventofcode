import sys


def dist(a, b):
    d = 0
    for i in range(len(a)):
        d += abs(a[i] - b[i])
    return d


def find_near(stars, p):
    cons = {p}
    busy = True
    while busy:
        busy = False
        for s in stars:
            if s in cons:
                continue
            for c in cons:
                if dist(s, c) <= 3:
                    cons.add(s)
                    busy = True
                    break
    return cons


lines = sys.stdin.readlines()
stars = set()
for l in lines:
    star = tuple(map(int, l.split(",")))
    stars.add(star)

n_cons = 0
while len(stars) > 0:
    for s in stars:
        break
    cons = find_near(stars, s)
    stars -= cons
    n_cons += 1
# 608 too high
print(n_cons)
