import sys


def append_path(paths, a, b):
    if b == "start" or a == "end":
        return
    if a not in paths:
        paths[a] = []
    paths[a].append(b)


def validate_road(road, end):
    if end[0].isupper():
        return True

    if end not in road:
        return True

    visited = dict()
    for r in road:
        if r[0].isupper():
            continue
        if r in visited:
            return False
        visited[r] = True
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
    road = roads.pop()
    for p in paths[road[-1]]:
        if p == "end":
            solutions.append(road + ["end"])
            continue
        if not validate_road(road, p):
            continue
        roads.append(road + [p])

print(len(solutions))
