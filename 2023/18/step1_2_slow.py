import sys


def print_map(mapa):
    min_line = int(min([x.real for x in mapa]))
    min_col = int(min([x.imag for x in mapa]))
    max_line = int(max([x.real for x in mapa]))
    max_col = int(max([x.imag for x in mapa]))
    for i in range(min_line, max_line + 1):
        out = ""
        for j in range(min_col, max_col + 1):
            if complex(i,j) == 0j:
                out +="*"
            elif complex(i, j) in mapa:
                out += "#"
            else:
                out += "."
        print(out)
    print("")

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


def calc_area(border):
    min_line = int(min([x.real for x in border]))
    min_col = int(min([x.imag for x in border]))
    max_line = int(max([x.real for x in border]))
    max_col = int(max([x.imag for x in border]))
    visited = set()
    todo = [complex(min_line - 1, min_col - 1)]
    while todo:
        pos_ini = todo.pop()
        visited.add(pos_ini)
        for dir in complex(0, 1), complex(0, -1), complex(1, 0), complex(-1, 0):
            pos = pos_ini + dir
            if pos in visited:
                continue
            if pos.real not in range(
                min_line - 1, max_line + 2
            ) or pos.imag not in range(min_col - 1, max_col + 2):
                continue
            if pos in border:
                continue
            todo.append(pos)
    print_map(border)
    # print_map(visited)
    return ((max_line + 3 - min_line) * (max_col + 3 - min_col)) - len(visited)

def calc_area_dir_lens(dir_lens):
 pos = complex(0, 0)
 border = set([pos])
 for dir, length in dir_lens:
    for _ in range(length):
        pos += dir
        border.add(pos)
 
 return calc_area(border)


lines = sys.stdin.readlines()
dir_lens = map(dirlen_decode, lines)
print("Part 1:", calc_area_dir_lens(dir_lens))

dir_lens = map(notcolor_decode, lines)
print("Part 2:", calc_area_dir_lens(dir_lens))