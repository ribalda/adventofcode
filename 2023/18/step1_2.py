import sys


def letter2dir(letter):
    return {
        "R": complex(0, 1),
        "L": complex(0, -1),
        "U": complex(-1, 0),
        "D": complex(1, 0),
    }[letter]


def dirlen_decode(line):
    dir, length = line.strip().split()[:2]
    dir = letter2dir(dir)
    length = int(length)
    return dir, length


def notcolor_decode(line):
    line = line.strip()
    notcolor = line.split()[2]
    dir = {
        "0": letter2dir("R"),
        "1": letter2dir("D"),
        "2": letter2dir("L"),
        "3": letter2dir("U"),
    }[notcolor[-2:-1]]
    length = int(notcolor[2:-2], 16)
    return dir, length


def calc_area(vertex):
    out = 0
    for idx, v in enumerate(vertex[:-1]):
        out += v.real * vertex[idx + 1].imag
        out -= v.imag * vertex[idx + 1].real
    out /= 2
    return int(abs(out))


def calc_area_dirlen(dir_lens):
    start = complex(0, 0)
    total_len = 0
    vertex = [start]
    extra_area = 0
    pos = start
    for dir, length in dir_lens:
        extra_area += length
        pos += length * dir
        total_len += length
        vertex.append(pos)
    if pos != start:
        vertex.append(start)
    return calc_area(vertex) + int(extra_area / 2) + 1


lines = sys.stdin.readlines()

dir_lens = map(dirlen_decode, lines)
print("Part 1:", calc_area_dirlen(dir_lens))

dir_lens = map(notcolor_decode, lines)
print("Part 2:", calc_area_dirlen(dir_lens))
