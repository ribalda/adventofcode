import sys
import heapq


def int2letter(v):
    return ["A", "B", "C", "D"][v]


def get_dests(v):
    if v == " " or v == ".":
        return None
    if v == "A":
        return set((11, 12))
    if v == "B":
        return set((13, 14))
    if v == "C":
        return set((15, 16))
    if v == "D":
        return set((17, 18))


def trip_val(l):
    if l == "A":
        return 1
    if l == "B":
        return 10
    if l == "C":
        return 100
    if l == "D":
        return 1000


def trip_len(mapa, i, d):
    n = 0

    if d >= 11:
        if (d - 11) % 2 == 1:
            if mapa[d] != ".":
                return -1
            n += 1
            d -= 1
        if mapa[d] != ".":
            return -1
        n += 1
        d -= 9

    if i >= 11:
        if (i - 11) % 2 == 1:
            if mapa[i - 1] != ".":
                return -1
            n += 1
            i -= 1
        n += 1
        i -= 9

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
    d = mapa[-8:]
    out = set()
    for i in range(4):
        if d[2 * i + 1] == int2letter(i) and d[2 * i] == ".":
            out.add(i * 2 + 11)
        if d[2 * i] == "." and d[2 * i + 1] == ".":
            out.add(i * 2 + 1 + 11)
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
        vdests = get_dests(mapa[i])
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
    if i > 11 and (i - 11) % 2 == 1:
        if i in get_dests(mapa[i]):
            return []
    if i > 11 and (i - 11) % 2 == 0:
        if i in get_dests(mapa[i]) and mapa[i] == mapa[i + 1]:
            return []
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
    v, mapa = s

    out = []
    for i, n in enumerate(mapa):
        if n == "." or n == " ":
            continue
        out += get_valid_states_i(s, i)

    return out


def debug(mapa):
    print(mapa[:11])
    out = [" "] * 11
    for i in range(4):
        out[2 + i * 2] = mapa[11 + 2 * i]
    print("".join(out))
    for i in range(4):
        out[2 + i * 2] = mapa[12 + 2 * i]
    print("".join(out))


lines = sys.stdin.readlines()
mapa = ".. . . . .."
for i in range(3, 10, 2):
    mapa += lines[2][i]
    mapa += lines[3][i]
v = 0

orig = mapa
todo = []
heapq.heappush(todo, (v, mapa))
visited = dict()
state_from = dict()
visited[mapa] = v


while todo:
    s = heapq.heappop(todo)
    v, mapa = s
    if mapa[-8:] == "AABBCCDD":
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

sys.exit(0)
while mapa != orig:
    print(" ")
    print(visited[mapa], " " * 10, mapa)
    debug(mapa)
    mapa = state_from[mapa]

print(" ")
print(0, mapa)
debug(mapa)

print(v)
