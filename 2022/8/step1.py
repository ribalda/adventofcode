import sys


def find_visible(forest, p0, step):
    out = set()
    maxv = forest[p0[0]][p0[1]]
    p1 = p0
    for _ in range(len(forest) - 1):
        p1 = (p1[0] + step[0], p1[1] + step[1])
        p1_val = forest[p1[0]][p1[1]]
        if p1_val > maxv:
            out.add(p1)
        maxv = max(maxv, p1_val)
    return out


forest = []
for l in sys.stdin.readlines():
    l = map(int, list(l[:-1]))
    forest.append(list(l))

L = len(forest)

step = 0
visible = set()


for line in range(1, L - 1):
    visible |= find_visible(forest, (line, 0), (0, 1))
    visible |= find_visible(forest, (line, L - 1), (0, -1))

for col in range(1, L - 1):
    visible |= find_visible(forest, (0, col), (1, 0))
    visible |= find_visible(forest, (L - 1, col), (-1, 0))

print(len(visible) + (L - 1) * 4)
