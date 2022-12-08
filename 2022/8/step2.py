import sys


def in_forest(forest, p1):
    if p1[0] < 0 or p1[0] >= len(forest):
        return False
    if p1[1] < 0 or p1[1] >= len(forest):
        return False
    return True


def max_distance(forest, p0, step):
    L = len(forest)
    out = 0

    p1 = (p0[0] + step[0], p0[1] + step[1])
    while in_forest(forest, p1):
        out += 1
        if forest[p0[0]][p0[1]] <= forest[p1[0]][p1[1]]:
            break
        p1 = (p1[0] + step[0], p1[1] + step[1])
    return out


def scenic_value(forest, p0):
    out = 1
    for dire in (0, 1), (0, -1), (1, 0), (-1, 0):
        out *= max_distance(forest, p0, dire)

    return out


forest = []
for l in sys.stdin.readlines():
    l = map(int, list(l[:-1]))
    forest.append(list(l))


L = len(forest)

max_scenic = 0
for line in range(L):
    for col in range(L):
        max_scenic = max(max_scenic, scenic_value(forest, (line, col)))

print(max_scenic)
