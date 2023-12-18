import sys
import math


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
        "0": complex(0, 1),
        "2": complex(0, -1),
        "3": complex(-1, 0),
        "1": complex(1, 0),
    }[notcolor[-2:-1]]
    length = int(notcolor[2:-2], 16)
    return dir, length


def calc_area(vertex):
    out = 0
    for idx, v in enumerate(vertex):
        step = vertex[(idx + 1) % len(vertex)].real + v.real
        step *= vertex[(idx + 1) % len(vertex)].imag - v.imag
        out += step
    out /= 2
    return abs(int(out))


def calc_area_dirlen(dir_lens):
    pos = complex(0, 0)
    total_len = 0
    vertex = [pos]
    extra_area = 1
    for dir, length in dir_lens:
        length = int(length)
        if dir in (complex(0,1), complex(1,0)):
            extra_area += length
        pos += length * dir
        total_len += length
        pos_in = pos
        vertex.append(pos_in)
    return calc_area(vertex) + extra_area


lines = sys.stdin.readlines()

dir_lens = map(dirlen_decode, lines)
print("Part 1:", calc_area_dirlen(dir_lens))

dir_lens = map(notcolor_decode, lines)
print("Part 2:", calc_area_dirlen(dir_lens))
