import sys


def debug(mapa):
    vals = []
    for i in range(L):
        o = ""
        for j in range(C):
            p = complex(i, j)
            if p in mapa:
                o += mapa[p][0]
                if mapa[p][0] in ["G", "E"]:
                    vals.append(mapa[p])
            else:
                o += "."
        print(o)
    print(vals)


def is_over(mapa):
    types = set()
    for p in mapa:
        if mapa[p][0] in ["G", "E"]:
            types.add(mapa[p][0])
    return len(types) != 2


def battle(mapa, p, power):
    movs = (-1, -1j, 1j, 1)
    minv = None
    for m in movs:
        p2 = p + m
        if p2 not in mapa:
            continue
        if mapa[p2][0] in ["G", "E"] and mapa[p2][0] != mapa[p][0]:
            if minv == None:
                minv = mapa[p2][1]
            minv = min(minv, mapa[p2][1])

    if minv == None:
        return False

    for m in movs:
        p2 = p + m
        if p2 not in mapa:
            continue
        if (
            mapa[p2][0] in ["G", "E"]
            and mapa[p2][0] != mapa[p][0]
            and mapa[p2][1] == minv
        ):
            if mapa[p2][0] == "E":
                power = 3
            mapa[p2] = mapa[p2][0], mapa[p2][1] - power
            if mapa[p2][1] <= 0 and mapa[p2][0] == "E":
                return None
            if mapa[p2][1] <= 0:
                del mapa[p2]
            return True


def move(mapa, p):
    todo = [p]
    visited = set(todo)
    parent = dict()

    while todo:
        t = todo.pop(0)
        movs = (-1, -1j, 1j, 1)
        for m in movs:
            t2 = t + m
            if t2 in visited:
                continue
            if t2 not in mapa:
                todo.append(t2)
                visited.add(t2)
                parent[t2] = t
                continue
            if mapa[t2][0] in ["G", "E"] and mapa[t2][0] != mapa[p][0]:
                parent[t2] = t
                while parent[t2] != p:
                    t2 = parent[t2]
                return t2
    return None


def play(mapa, p, v):
    if p not in mapa:
        return None
    o = battle(mapa, p, v)
    if o == None:
        return None
    elif o == True:
        return p
    p2 = move(mapa, p)
    if p2 == None:
        return p

    mapa[p2] = mapa[p]
    del mapa[p]
    o = battle(mapa, p2, v)
    if o == None:
        return None
    return p2


def cycle(mapa, v):
    players = []
    for p in mapa:
        if mapa[p][0] in ["G", "E"]:
            players.append(p)
    players = sorted(players, key=lambda x: x.real * C + x.imag)
    endpos = set()
    for p in players:
        if p in endpos:
            continue
        if is_over(mapa):
            return False
        if p not in mapa:
            continue
        p2 = play(mapa, p, v)
        if p2 == None:
            return None
        endpos.add(p2)
    return True


def cycleval(mapa_in, v):
    mapa = mapa_in.copy()

    n_cycles = 0
    while True:
        o = cycle(mapa, v)
        if o == None:
            return None
        if o == False:
            break
        n_cycles += 1

    print(n_cycles)
    debug(mapa)
    val = 0
    for p in mapa:
        if mapa[p][0] in ["G", "E"]:
            val += mapa[p][1]

    return val * n_cycles


lines = sys.stdin.readlines()
mapa = dict()
for i, line in enumerate(lines):
    for j, l in enumerate(line):
        if l in ["G", "E", "#"]:
            mapa[complex(i, j)] = (l, 200)
L, C = i + 1, j + 1


v = 3
while True:
    v += 1
    print(v)
    r = cycleval(mapa, v)
    if r:
        print(r)
        break
