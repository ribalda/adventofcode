import sys


def append_path(paths, a, b):
    if a not in paths:
        paths[a] = []
    paths[a].append(b)


def validate_road(road, end):
    if end[0].isupper():
        return True
    for r in road:
        if r == end:
            return False
    return True


paths = dict()

for l in sys.stdin.readlines():
    a, b = l.strip().split("-")
    append_path(paths, a, b)
    append_path(paths, b, a)

solutions = []
roads = [["start"]]

while roads:
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
