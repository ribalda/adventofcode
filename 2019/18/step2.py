import sys


def visit(mapa, visited, keys, pos_a, nkeys, nsteps):
    if nsteps >= visited["max"]:
        return None
    if len(keys) == nkeys:
        if nsteps >= visited["max"]:
            return None
        visited["max"] = nsteps
        print(nsteps, keys)
        return [nsteps, keys]

    ret = None
    for i in range(4):
        for s in [1, -1, 1j, -1j]:
            p = pos_a[:]
            p[i] += s

            if mapa[p[i]] == "#":
                continue

            if mapa[p[i]].isupper() and mapa[p[i]].lower() not in keys:
                #print(mapa[p[i]], keys)
                continue

            k0 = keys[:]
            if mapa[p[i]].islower() and mapa[p[i]] not in k0:
                k0 += [mapa[p[i]]]

            ns = nsteps + 1
            if p[i] not in visited:
                visited[p[i]] = dict()
            ks = str(sorted(k0))
            if ks in visited[p[i]] and visited[p[i]][ks] <= ns:
                continue
            # if mapa[p[i]].islower():
            #    print(k0)
            visited[p[i]][ks] = ns
            r = visit(mapa, visited, k0, p, nkeys, ns)
            #r = None
            if r == None:
                continue

            if ret == None:
                ret = r

            if r[0] < ret[0]:
                ret = r

    return ret


def print_map_visited(map, visited):
    i = 0
    while i in mapa:
        j = 0
        s = ""
        while complex(i, j) in mapa:
            if complex(i, j) in visited:
                s += "*"
            else:
                if mapa[complex(i, j)] == ".":
                    s += " "
                else:
                    s += mapa[complex(i, j)]
            j += 1
        print(s)
        i += 1


lines = sys.stdin.readlines()

mapa = dict()
pos0 = None
k = list()
for i in range(len(lines)):
    for j in range(len(lines[i][:-1])):
        v = lines[i][j]
        p = complex(i, j)
        if v == "@":
            pos0 = p
            v = "."
        if v not in [".", "#"]:
            if v.islower():
                if v in k:
                    print(error)
                k += [v]
        mapa[p] = v

nkeys = len(k)
sys.setrecursionlimit(1500000)

pos_a = list()
for i in range(-1, 2):
    for j in range(-1, 2):
        p = pos0 + complex(i, j)
        if (abs(i) + abs(j)) == 2:
            mapa[p] = "."
            pos_a.append(p)
        else:
            mapa[p] = "#"

print(pos_a, nkeys)
visited = dict()
for p in pos_a:
    visited[p] = dict()
    visited[p][str([])] = 0
visited["max"] = 100000
ret = visit(mapa, visited, [], pos_a, nkeys, 0)
print(ret)

print_map_visited(mapa, visited)
