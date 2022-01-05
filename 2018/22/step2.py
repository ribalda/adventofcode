from functools import cache
import heapq

#dest, depth = 10 + 10j, 510
dest, depth = 13 + 704j, 9465
base = 20183
#t c n
#rocky,  wet,    narrow
#c or t, c or n, t or n  

valid_tools = {0,1}, {1,2}, {0,2}

@cache
def erosion(pos):
    if pos == 0:
        return depth
    if pos == dest:
        return depth
    if pos.imag == 0:
        return (int(pos.real) * 16807 + depth) % base
    if pos.real == 0:
        return (int(pos.imag) * 48271 + depth) % base
    return (erosion(pos-1) * erosion(pos-1j) + depth) % base

state = 0, 0, 0, 0
todo = []
heapq.heappush(todo, state)
visited = dict()
visited[(0,0)] = 0
while True:
    #print(todo)
    minutes, tool, posx, posy = heapq.heappop(todo)
    pos=complex(posx, posy)
    if pos == dest:
        if tool != 0:
            minutes += 7
            heapq.heappush(todo, (minutes, tool, pos.real, pos.imag))
            continue
        print(minutes)
        break
    tile = erosion(pos) % 3
    for tool2 in valid_tools[tile]:
        for mov in 1,-1,-1j,1j:
            pos2 = pos + mov
            if pos2.real < 0 or pos2.imag < 0:
                continue
            tile2 = erosion(pos2) % 3
            if tool2 not in valid_tools[tile2]:
                continue
            if tool2 == tool:
                minutes2 = minutes + 1
            else:
                minutes2 = minutes + 8
            v = pos2, tool2
            if v in visited and visited[v] <= minutes2:
                continue
            visited[v] = minutes2
            heapq.heappush(todo, (minutes2, tool2, pos2.real, pos2.imag))