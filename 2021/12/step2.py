import sys


def append_path(paths, a, b):
    if a not in paths:
        paths[a] = []
    paths[a].append(b)


def validate_road(road, end):
    if end[0].isupper():
        return True

    if end == "start":
        return False

    visited = dict()
    visited[end] = True
    n_two = 0
    for r in road:
        if r[0].isupper():
            continue
        if r not in visited:
            visited[r] = True
        else:
            n_two += 1
            if n_two == 2:
                return False
    return True


paths = dict()

for l in sys.stdin.readlines():
    a, b = l.strip().split("-")
    append_path(paths, a, b)
    append_path(paths, b, a)

solutions = []
roads = [["start"]]

l_s = 0
while roads:
    # progress
    if solutions and len(solutions[-1]) != l_s:
        l_s = len(solutions[-1])
        print(l_s, len(solutions), solutions[-1])

    road = roads[0]
    roads = roads[1:]
    for p in paths[road[-1]]:
        if p == "end":
            solutions.append(road + ["end"])
            continue
        if not validate_road(road, p):
            continue
        roads.append(road + [p])

print(len(solutions))
