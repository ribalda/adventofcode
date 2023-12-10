import sys
import heapq


def draw2movs(draw):
    conv = {
        "|": (complex(-1, 0), complex(1, 0)),
        "-": (complex(0, 1), complex(0, -1)),
        "L": (complex(-1, 0), complex(0, 1)),
        "J": (complex(-1, 0), complex(0, -1)),
        "7": (complex(1, 0), complex(0, -1)),
        "F": (complex(1, 0), complex(0, 1)),
        "S": (complex(1, 0), complex(0, 1)),
    }
    return conv[draw]


def connected(mapa, new_pos, pos):
    if new_pos not in mapa:
        return False
    for m in draw2movs(mapa[new_pos]):
        if new_pos + m == pos:
            return True
    return False


def get_loop(mapa, start):
    visited = {start: 0}
    dummy = 0
    nextmovs = [(0, dummy, start)]
    while nextmovs:
        steps, _, pos = heapq.heappop(nextmovs)
        steps += 1
        for m in draw2movs(mapa[pos]):
            new_pos = pos + m
            if visited.get(new_pos, steps + 1) < steps:
                continue
            if not connected(mapa, new_pos, pos):
                continue
            visited[new_pos] = steps
            dummy += 1
            heapq.heappush(nextmovs, (steps, dummy, new_pos))
    return visited


def n_inners(mapa, loop):
    out = 0
    loop_lines = sorted([x.real for x in loop])
    loop_cols = sorted([x.imag for x in loop])
    for line in range(int(loop_lines[-1])):
        cross = 0
        last_half = None
        for col in range(int(loop_cols[-1])):
            pos = complex(line, col)
            if pos not in loop or pos not in mapa:
                if (cross % 2) == 1:
                    out += 1
                continue
            val = mapa[pos]
            if val == "-":
                continue
            if val == "|":
                cross += 1
                continue
            if last_half == None:
                last_half = val
                continue
            if (last_half == "L" and val == "7") or (last_half == "F" and val == "J"):
                cross += 1
            last_half = None
    return out


mapa = dict()
for x, line in enumerate(sys.stdin.readlines()):
    for j, val in enumerate(line.strip()):
        if val == ".":
            continue
        pos = complex(x, j)
        if val == "S":
            start = pos
            val = "F"
        mapa[pos] = val

loop = get_loop(mapa, start)

print("Step1:", max(loop.values()))
print("Step2:", n_inners(mapa, set(loop.keys())))
