import sys
from collections import deque
from collections import defaultdict


def calculate_next(map_val, dir):
    conv_table = {
        ".": {
            complex(0, 1): (complex(0, 1),),
            complex(0, -1): (complex(0, -1),),
            complex(1, 0): (complex(1, 0),),
            complex(-1, 0): (complex(-1, 0),),
        },
        "-": {
            complex(0, 1): (complex(0, 1),),
            complex(0, -1): (complex(0, -1),),
            complex(1, 0): (complex(0, -1), complex(0, 1)),
            complex(-1, 0): (complex(0, -1), complex(0, 1)),
        },
        "|": {
            complex(0, 1): (complex(-1, 0), complex(1, 0)),
            complex(0, -1): (complex(-1, 0), complex(1, 0)),
            complex(1, 0): (complex(1, 0),),
            complex(-1, 0): (complex(-1, 0),),
        },
        "/": {
            complex(0, 1): (complex(-1, 0),),
            complex(0, -1): (complex(1, 0),),
            complex(1, 0): (complex(0, -1),),
            complex(-1, 0): (complex(0, 1),),
        },
        "\\": {
            complex(0, 1): (complex(1, 0),),
            complex(0, -1): (complex(-1, 0),),
            complex(1, 0): (complex(0, 1),),
            complex(-1, 0): (complex(0, -1),),
        },
    }
    return conv_table[map_val][dir]


def steps_mapa(mapa, pos_in, dir_in):
    visited = defaultdict(set)
    todo = deque([(pos_in, dir_in)])
    while todo:
        pos, dir = todo.pop()
        if pos not in mapa:
            continue
        if dir in visited[pos]:
            continue
        dirs = calculate_next(mapa[pos], dir)
        for d in dirs:
            p_new = pos + d
            if p_new not in mapa:
                continue
            if d in visited[p_new]:
                continue
            todo.append((p_new, d))
        visited[pos].add(dir)

    return len(visited)


def steps_mapa_all_dir(mapa, pos):
    out = 0
    for dir in complex(0, 1), complex(0, -1), complex(1, 0), complex(-1, 0):
        if pos.real == 0 and dir.real == -1:
            continue
        if pos.real != 0 and dir.real == 1:
            continue
        if pos.imag == 0 and dir.imag == -1:
            continue
        if pos.imag != 0 and dir.imag == 1:
            continue
        out = max(steps_mapa(mapa, pos, dir), out)
    return out


mapa = {}
lines = sys.stdin.readlines()
for idx, line in enumerate(lines):
    for jdx, v in enumerate(line.strip()):
        mapa[complex(idx, jdx)] = v

print("Part 1:", steps_mapa(mapa, complex(0, 0), complex(0, 1)))
max_val = 0
for l in range(len(lines)):
    max_val = max(steps_mapa_all_dir(mapa, complex(l, 0)), max_val)
    max_val = max(steps_mapa_all_dir(mapa, complex(l, len(lines[0]) - 1)), max_val)
for c in range(len(lines[0])):
    max_val = max(steps_mapa_all_dir(mapa, complex(0, c)), max_val)
    max_val = max(steps_mapa_all_dir(mapa, complex(len(lines) - 1, c)), max_val)
print("Part 2:", max_val)
