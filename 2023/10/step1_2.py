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


def n_cross(mapa, loop, p0):
    out = 0
    last_half = None
    pos = complex(p0.real, 0)
    while pos != p0:
        if pos not in loop:
            pos += 1j
            continue
        val = mapa.get(pos)
        pos += 1j
        if val == "-":
            continue
        if val == "|":
            out += 1
            continue
        if last_half == None:
            last_half = val
            continue
        if (last_half == "L" and val == "7") or (last_half == "F" and val == "J"):
            out += 1
        last_half = None
    return out


def paint(mapa, visited, loop, pos):
    if pos in visited or pos in loop:
        return set()

    nextpos = [pos]
    inside = set()

    mapa_lines = sorted([x.real for x in mapa])
    mapa_cols = sorted([x.imag for x in mapa])

    while nextpos:
        pos = nextpos.pop()
        if pos in inside:
            continue
        if pos in loop:
            continue
        if pos in visited:
            return set()
        visited.add(pos)
        if (
            pos.real < mapa_lines[0]
            or pos.real > mapa_lines[-1]
            or pos.imag < mapa_cols[0]
            or pos.imag > mapa_cols[-1]
        ):
            return set()
        inside.add(pos)
        for p in (complex(0, 1), complex(0, -1), complex(1, 0), complex(-1, 0)):
            nextpos.append(pos + p)

    if len(inside) == 0:
        return set()

    # Is it realy inside?
    for i in inside:
        if (n_cross(mapa, loop, i) % 2) == 0:
            return set()
        return inside


def get_inners(mapa, loop):
    visited = set()
    inside = set()
    for _, l in enumerate(loop):
        for p in (complex(0, 1), complex(0, -1), complex(1, 0), complex(-1, 0)):
            inside |= paint(mapa, visited, loop, l + p)
    return inside


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
print("Step2:", len(get_inners(mapa, set(loop.keys()))))
