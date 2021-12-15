import sys
import heapq

def complex2int(origin):
    return int(L_S*origin.real+origin.imag)

def int2complex(n):
    return complex(n//(L*S), n%(L*S))

def get_distance(origin, end, mapa):
    to_visit = [(0,complex2int(origin))]
    distance = {origin: 0}

    while to_visit:
        #print(to_visit)
        d,n = heapq.heappop(to_visit)
        n = int2complex(n)
        if d > distance[n]:
            continue
        for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_n = n + complex(i, j)
            if next_n not in mapa:
                continue
            new_dist = distance[n] + mapa[next_n]
            if next_n in distance and distance[next_n] <= new_dist:
                continue
            distance[next_n] = new_dist
            if next_n == end:
                return distance[end]
            
            heapq.heappush(to_visit, (distance[next_n], complex2int(next_n)))

    return distance[end]


mapa = dict()
lines = sys.stdin.readlines()
L = len(lines)
S = 5
L_S = L * S
for i, line in enumerate(lines):
    for j, l in enumerate(line.strip()):
        for ii in range(S):
            for jj in range(S):
                v = (((int(l) + ii + jj) -1 ) % 9 ) + 1
                mapa[complex(i+ii*L, j+jj*L)] = v

print(get_distance(0j, complex(S*L-1, S*L-1), mapa))
