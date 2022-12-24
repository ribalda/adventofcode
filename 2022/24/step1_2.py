import sys
from collections import deque

BLIZ = {">": 1j, "<": -1j, "^": -1, "v": +1}


def print_map(mapa, e):
    for l in range(L):
        print("#", end="")
        for c in range(C):
            if complex(l, c) == e:
                print("E", end="")
                continue
            if complex(l, c) in mapa:
                print(".", end="")
            else:
                print("*", end="")
        print("#")


def inctime(time):
    tL = (time[0] + 1) % L
    tC = (time[1] + 1) % C
    return (tL, tC)


def blizards2mapa(blizards):
    mapa = set()
    blizpos = set([b[0] for b in blizards])
    for l in range(L):
        for c in range(C):
            p0 = complex(l, c)
            if p0 not in blizpos:
                mapa.add(p0)
    mapa.add(complex(-1, 0))
    mapa.add(complex(L, C - 1))
    return mapa


def blizards_step(blizards):
    out = []
    for pos, dir in blizards:
        pos += dir
        pos = complex(int(pos.real) % L, int(pos.imag) % C)
        out.append((pos, dir))
    return out


def travel_steps(mapas, time, start, end):
    # steps, p, time
    s0 = (0, start, time)
    visited = set()

    todo = deque([s0])
    while todo:
        steps, pos, time = todo.popleft()

        steps1 = steps + 1
        time1 = inctime(time)
        for mov in [-1j, 1j, 1, -1, 0]:
            pos1 = pos + mov

            # end!
            if pos1 == end:
                return (steps1, time1)

            # Not a empty space
            if pos1 not in mapas[time1]:
                continue

            # Visited
            v = pos1, time1
            if v in visited:
                continue

            visited.add(v)
            s1 = steps1, pos1, time1
            todo.append(s1)
    return None


lines = sys.stdin.readlines()
L = len(lines) - 2
C = len(lines[0]) - 3  # \n

blizards = []
lines = lines[1:-1]
for l, line in enumerate(lines):
    line = line[1:-1]
    if line[-1] == "#":
        line = line[:-1]
    for c, col in enumerate(line):
        if col == ".":
            continue
        bli = (complex(l, c), BLIZ[col])
        blizards.append(bli)


mapas = {}
time = (0, 0)
while time not in mapas:
    mapas[time] = blizards2mapa(blizards)
    blizards = blizards_step(blizards)
    time = inctime(time)

start = complex(-1, 0)
end = complex(L, C - 1)
steps = 0

time = (0, 0)
s1, time = travel_steps(mapas, time, start, end)
steps += s1
print("Step 1:", steps)
s1, time = travel_steps(mapas, time, end, start)
steps += s1
s1, time = travel_steps(mapas, time, start, end)
steps += s1
print("Step 2:", steps)
