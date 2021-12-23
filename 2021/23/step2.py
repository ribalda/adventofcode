import sys
import heapq

N = 4
if len(sys.argv) >= 2:
    N = int(sys.argv[1])


def int2letter(v):
    return ["A", "B", "C", "D"][v]


def get_dests():
    d = dict()
    d[" "] = None
    d["."] = None
    idx = 11
    for i in "A", "B", "C", "D":
        o = []
        for _ in range(N):
            o.append(idx)
            idx += 1
        d[i] = set(o)
    return d


DESTS = get_dests()


def trip_val(l):
    return {"A": 1, "B": 10, "C": 100, "D": 1000}[l]


def all_clean(mapa, i, j):
    for k in range(i, j + 1):
        if mapa[k] != ".":
            return False
    return True


def to_corridor(n):
    n -= 11
    n //= N
    n *= 2
    n += 2
    return n


def get_corridors():
    out = dict()
    for i in range(4):
        n = 11 + i * N
        out[n] = to_corridor(n)
    return out


CORRIDOR = get_corridors()


def trip_len(mapa, i, d):
    n = 0

    if d >= 11:
        first = d - (d - 11) % N
        if not all_clean(mapa, first, d):
            return -1
        n += d - first + 1
        d = CORRIDOR[first]

    if i >= 11:
        first = i - (i - 11) % N
        if i != first:
            if not (all_clean(mapa, first, i - 1)):
                return -1
        n += i - first + 1
        i = CORRIDOR[first]

    if d > i:
        for j in range(i + 1, d + 1, 1):
            if mapa[j] != "." and mapa[j] != " ":
                return -1
            n += 1
    else:
        for j in range(i - 1, d - 1, -1):
            if mapa[j] != "." and mapa[j] != " ":
                return -1
            n += 1
    return n


def get_open_dest(mapa):
    out = set()
    for i in range(4):
        for j in range(N):
            if mapa[11 + i * N + j] != ".":
                continue
            for k in range(j + 1, N):
                if mapa[11 + i * N + k] == "." or mapa[11 + i * N + k] != int2letter(i):
                    break
            else:
                out.add(11 + i * N + j)
                break
    return out


def move(mapa, o, d):
    mapa = list(mapa)
    mapa[d] = mapa[o]
    mapa[o] = "."
    return "".join(mapa)


def get_dest_state(s):
    v, mapa = s
    open_dests = get_open_dest(mapa)
    for i in range(len(mapa)):
        vdests = DESTS[mapa[i]]
        if vdests == None or (i in vdests):
            continue
        vdests = open_dests & vdests
        if not vdests:
            continue
        d = vdests.pop()
        l = trip_len(mapa, i, d)
        if l < 0:
            continue
        v += l * trip_val(mapa[i])
        mapa = move(mapa, i, d)
        return (v, mapa)


def get_valid_states_i(s, i):
    v, mapa = s
    out = []
    for j in range(11):
        if mapa[j] != "." or j == i:
            continue
        if i < 11 and j < 11:
            continue
        l = trip_len(mapa, i, j)
        if l < 0:
            continue

        if l > 0:
            v2 = v + l * trip_val(mapa[i])
            mapa2 = move(mapa, i, j)
            out.append((v2, mapa2))
    return out


def get_valid_states(s):
    _, mapa = s

    out = []
    for i, n in enumerate(mapa):
        if n == "." or n == " ":
            continue
        out += get_valid_states_i(s, i)

    return out


def get_end(n):
    out = ""
    for i in "A", "B", "C", "D":
        for _ in range(n):
            out += i
    return out


def debug(mapa):
    print(mapa[:11])
    out = [" "] * 11
    for l in range(N):
        for i in range(4):
            out[2 + i * 2] = mapa[11 + N * i + l]
        print("".join(out))


lines = sys.stdin.readlines()
mapa = ".. . . . .."
for i in range(3, 10, 2):
    for j in range(N):
        mapa += lines[2 + j][i]
v = 0

orig = mapa
todo = []
heapq.heappush(todo, (v, mapa))
visited = dict()
state_from = dict()
end = get_end(N)
debug(mapa)

while todo:
    s = heapq.heappop(todo)
    v, mapa = s
    if mapa[-len(end) :] == end:
        print(v)
        break

    t = get_dest_state(s)
    if t != None:
        if t[1] not in visited or visited[t[1]] > t[0]:
            heapq.heappush(todo, t)
            visited[t[1]] = t[0]
            state_from[t[1]] = mapa
        continue
    states = get_valid_states(s)
    for t in states:
        if t[1] not in visited or visited[t[1]] > t[0]:
            heapq.heappush(todo, t)
            visited[t[1]] = t[0]
            state_from[t[1]] = mapa
while mapa != orig:
    print(" ")
    print(visited[mapa])
    debug(mapa)
    mapa = state_from[mapa]

print(" ")
print(0)
debug(mapa)

print(v)
