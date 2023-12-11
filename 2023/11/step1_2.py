import sys


def all_dots(line):
    line = map(lambda x: x == ".", line.strip())
    return line


def get_empty(lines):
    out = []
    lines = map(all_dots, lines)
    for idx, l in enumerate(lines):
        if all(l):
            out.append(idx)
    return set(out)


def transpose(lines):
    out = []
    for i in range(len(lines[0].strip())):
        out.append("".join([x[i] for x in lines]))
    return out


def get_points(lines):
    out = []
    for i, line in enumerate(lines):
        for j, val in enumerate(line):
            if val == "#":
                out.append(complex(i, j))
    return out


def distance_axis(a, b, empty, expand):
    fr = int(min(a, b))
    to = int(max(a, b))
    out = to - fr
    extra = 0
    for i in range(fr + 1, to):
        if i in empty:
            extra += expand - 1

    return out + extra


def distance(fr, to, empty_lines, empty_cols, expand):
    out = distance_axis(to.real, fr.real, empty_lines, expand)
    out += distance_axis(to.imag, fr.imag, empty_cols, expand)
    return out


def all_distances(points, empty_lines, empty_cols, expand):
    out = 0
    for idx, fr in enumerate(points):
        for to in points[idx + 1 :]:
            out += distance(fr, to, empty_lines, empty_cols, expand)
    return out


lines = sys.stdin.readlines()
empty_lines = get_empty(lines)
empty_cols = get_empty(transpose(lines))
points = get_points(lines)

print("Part1:", all_distances(points, empty_lines, empty_cols, 2))
print("Part2:", all_distances(points, empty_lines, empty_cols, 1000000))
