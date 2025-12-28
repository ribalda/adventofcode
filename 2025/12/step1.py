import sys


def get_regions(line):
    size, shapes = line.split(": ")
    x_y = tuple(map(int, size.split("x")))
    shapes = tuple(map(int, shapes.split(" ")))
    return (complex(x_y[0], x_y[1]), shapes)


def rot_shape(shape):
    out = set()
    for i in range(3):
        for j in range(3):
            p = complex(j, 2 - i)
            if p in shape:
                out.add(complex(i, j))
    return out


def get_shape(shape):
    out = set()
    for x, line in enumerate(shape.splitlines()[1:]):
        for y, v in enumerate(line.strip()):
            if v == "#":
                out.add(complex(x, y))

    a = out
    b = rot_shape(a)
    c = rot_shape(b)
    d = rot_shape(c)

    return (a, b, c, d)


def add_shape(world, shape, offset):
    out = set()
    for p in shape:
        p += offset
        if p in world:
            return None
        out.add(p)
    return world | out


def valid_shape_count(world, size, shapes, shape_count):
    for i, s in enumerate(shape_count):
        if s == 0:
            continue
        new_shape_count = list(shape_count)
        new_shape_count[i] -= 1
        new_shape_count = tuple(new_shape_count)
        for l in range(0, int(size.real) - 2):
            for c in range(0, int(size.imag) - 2):
                for r in range(4):
                    new_world = add_shape(world, shapes[i][r], complex(l, c))
                    if new_world == None:
                        continue
                    return valid_shape_count(new_world, size, shapes, new_shape_count)
        return False
    return True


def part1(shapes, regions):
    out = 0
    for r in regions:
        if valid_shape_count(set(), r[0], shapes, r[1]):
            out += 1
    return out


paragraphs = sys.stdin.read().split("\n\n")
regions = tuple(map(get_regions, paragraphs[-1].splitlines()))
shapes = tuple(map(get_shape, paragraphs[:-1]))

print("Part 1:", part1(shapes, regions))
