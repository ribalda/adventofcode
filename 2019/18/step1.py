import sys


def visit(mapa, visited, keys, pos, nkeys, nsteps):
    if len(keys) == nkeys:
        return [nsteps, keys]

    ret = None
    for k in [1, -1, 1j, -1j]:
        p = pos + k
        if mapa[p] == "#":
            continue

        if mapa[p].isupper() and mapa[p].lower() not in keys:
            print(mapa[p], keys)
            continue

        k0 = keys[:]
        if mapa[p].islower() and mapa[p] not in k0:
            k0 += [mapa[p]]

        ns = nsteps + 1
        if p not in visited:
            visited[p] = dict()
        ks = str(sorted(k0))
        if ks in visited[p] and visited[p][ks] <= ns:
            continue
        if mapa[p].islower():
            print(k0)
        visited[p][ks] = ns
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
pos = None
k = list()
for i in range(len(lines)):
    for j in range(len(lines[i][:-1])):
        v = lines[i][j]
        p = complex(i, j)
        if v == "@":
            pos = p
            v = "."
        if v not in [".", "#"]:
            if v.islower():
                if v in k:
                    print(error)
                k += [v]
        mapa[p] = v

nkeys = len(k)
sys.setrecursionlimit(1500000)

print(pos, nkeys)
visited = dict()
visited[pos] = dict()
visited[pos][str([])] = 0
ret = visit(mapa, visited, [], pos, nkeys, 0)
print(ret)

print_map_visited(map, visited)