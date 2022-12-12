import sys

visited = dict()
todo = []
mapa = dict()
for l, line in enumerate(sys.stdin.readlines()):
    for c, v in enumerate(line):
        p = complex(l, c)
        mapa[p] = ord(v)
        if v == "E":
            todo.append((0, p))
            visited[p] = 0
            mapa[p] = ord("z")
        if v == "S":
            mapa[p] = ord("a")


while todo:
    step, pos = todo.pop(0)
    for mov in 1, -1, -1j, +1j:
        new_pos = pos + mov
        if new_pos not in mapa:
            continue
        if mapa[pos] > (mapa[new_pos] + 1):
            continue
        if mapa[new_pos] == ord("a"):
            print(step + 1)
            sys.exit(0)
        if new_pos in visited:
            continue
        todo.append((step + 1, new_pos))
        visited[new_pos] = new_pos
