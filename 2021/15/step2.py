import sys


def debug(L, mapa):
    print("===")
    for i in range(L):
        out = ""
        for j in range(L):
            if complex(i, j) not in mapa:
                out += "  *"
            else:
                out += format(mapa[complex(i, j)], '3d')
        print(out)
    print("")


def pop_min(to_visit, distance):
    min_idx = 0
    for i, v in enumerate(to_visit):
        if distance[v] < distance[to_visit[min_idx]]:
            min_idx = i
    return to_visit.pop(min_idx)


def get_distance(origin, end, mapa):
    to_visit = [origin]
    distance = {origin: 0}

    while to_visit:
        n = pop_min(to_visit, distance)
        for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_n = n + complex(i, j)
            if next_n not in mapa:
                continue
            new_dist = distance[n] + mapa[next_n]
            if next_n in distance and distance[next_n] <= new_dist:
                continue
            distance[next_n] = new_dist
            if next_n != end:
                to_visit += [next_n]
            else:
                return distance[end]

    return distance[end]


mapa = dict()
lines = sys.stdin.readlines()
for i, line in enumerate(lines):
    for j, l in enumerate(line.strip()):
        for ii in range(5):
            for jj in range(5):
                v = int(l) + ii + jj
                if v > 9:
                    v -= 9
                mapa[complex(i+ii*len(lines), j+jj*len(lines))] = v

print(get_distance(0j, complex(len(lines*5)-1, len(lines*5)-1), mapa))
