import sys

visited = dict()
todo = []
mapa = dict()
for l, line in enumerate(sys.stdin.readlines()):
    for c, v in enumerate(line):
        p = complex(l, c)
        mapa[p] = ord(v)
        if v == "S":
            todo.append((0, p))
            visited[p] = 0
            mapa[p] = ord("a")
        if v == "E":
            end = p
            mapa[p] = ord("z")


while todo:
    step, pos = todo.pop(0)
    for mov in 1, -1, -1j, +1j:
        new_pos = pos + mov
        if new_pos not in mapa:
            continue
        if new_pos in visited:
            continue
        if mapa[new_pos] > (mapa[pos] + 1):
            continue
        if new_pos == end:
            print(step + 1)
            sys.exit(0)
        todo.append((step + 1, new_pos))
        visited[new_pos] = new_pos
