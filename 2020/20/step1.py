import sys
import math


def validate_last(pieces, size):
    if len(pieces) < 2:
        return True

    last = len(pieces) - 1
    for p in pieces[0:-1]:
        if pieces[last][0] == p[0]:
            return False

    if last % size:
        if pieces[last][1][3] != pieces[last-1][1][1]:
            return False

    if last >= size:
        if pieces[last][1][0] != pieces[last-size][1][2]:
            return False
    return True


def find_order(order_tiles, pieces, size):
    if len(order_tiles) == (size * size):
        return order_tiles
    for t in pieces:
        if validate_last(order_tiles+[t], size):
            r = find_order(order_tiles+[t], pieces, size)
            if r != []:
                return r
    return []


def rotate(edges):
    out = []
    out.append(edges[3][::-1])
    out.append(edges[0])
    out.append(edges[1][::-1])
    out.append(edges[2])
    return out


def flip_horver(edges):
    return edges[::-1]


def toint(a):
    b = ""
    for s in a:
        if s == "#":
            b += "1"
        else:
            b += "0"
    return int(b, 2)


tiles = sys.stdin.read().split("\n\n")

SIZE = int(math.sqrt(len(tiles)))

# [N,[edges]]
pieces = list()
for t in tiles:
    lines = t.split("\n")
    if len(lines) == 1:
        break
    n = lines[0].split(" ")[1][:-1]
    n = int(n)
    top = lines[1]
    down = lines[-1]
    left = ""
    right = ""
    for l in lines[1:]:
        left += l[0]
        right += l[-1]
    edges = [top, right, down, left]
    # make use of symetry
    for i in range(4):
        pieces.append([n, list(map(toint, edges))])
        pieces.append([n, list(map(toint, flip_horver(edges)))])
        edges = rotate(edges)

order = find_order([], pieces, SIZE)
print(order)
print(order[0][0]*order[SIZE-1][0]*order[-SIZE][0]*order[-1][0])
