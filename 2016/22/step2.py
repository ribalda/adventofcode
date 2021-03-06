import sys
import copy

X = 38
Y = 28
#X = 3
#Y = 3

used = list()
for y0 in range(Y):
    x =[]
    for x0 in range(X):
        x += [0]
    used +=[x]

size = copy.deepcopy(used)

for l in sys.stdin.readlines()[2:]:
    l = l.split()
    us = int(l[2][:-1])
    si = int(l[1][:-1])
    name = l[0].split("-")
    x = int(name[1][1:])
    y = int(name[2][1:])
    used[y][x] = us
    size[y][x] = si

def h(a,b):
    return a[0] |  a[1] <<8 | b[0] <<16 | b[1] << 24

def movements(used,zero):
    mov = list()
    pos = [[-1,0],[1,0],[0,-1],[0,1]]
    x = zero[1]
    y = zero[0]
    for p in pos:
        y0 = zero[0]+p[0]
        x0 = zero[1]+p[1]
        if x0<0 or x0 >=X or y0<0 or y0 >=Y:
            continue
        if used[y0][x0] <= size[y][x]:
            m = [[y0,x0] ,[y,x]]
            mov += [m]

    return mov

def findz(used):
    for y in range(Y):
        for x in range(X):
            if used[y][x] == 0:
                return [y,x]

data = [0,X-1]
ze = findz(used)
state = [data,ze,used,0]

work =[state]

visited = dict()
ha = h(data,ze)
visited[ha] = True

last_step = 0
while len(work) > 0:
    s =work[0]
    work = work[1:]

    [data,zero,used,steps] = s

    if steps > last_step:
        last_step = steps
        print (steps, len(work), zero, data)

    if data == [0,0]:
        print steps
        break

    mov = movements(used,zero)
    for m in mov:
        #print m
        s2 = copy.deepcopy(s)
        [data,zero,used,steps] = s2
        used[m[1][0]][m[1][1]] = used[m[0][0]][m[0][1]]
        used[m[0][0]][m[0][1]] = 0
        if [m[0][0],m[0][1]] == data:
            data = [m[1][0],m[1][1]]
        zero = [m[0][0],m[0][1]]
        ha = h(data,zero)
        if ha in visited:
            continue
        visited[ha] = True
        s2 = [data,zero,used,steps+1]
        work += [s2]



