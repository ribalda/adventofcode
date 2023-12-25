import sys
from collections import defaultdict


def print_links(links):

    print("digraph G {")
    for fr in links:
        for to in links[fr]:
            print(fr, "->", to)
    print("}")




links = defaultdict(set)
for line in sys.stdin.readlines():
    line= line.strip()
    fr, tos = line.split(": ")
    tos = tos.split(" ")
    for to in tos:
        links[fr].add(to)
        links[to].add(fr)

lens = [len(links[x]) for x in links]

cross_links = (("zvk","sxx"),("njx","pbx"),("sss","pzr"))
for a,b in cross_links:
    links[a].remove(b)
    links[b].remove(a)


visited = set()
start = a

todo = [a]
while todo:
    t = todo.pop()
    if t in visited:
        continue
    for s in links[t]:
        if s in visited:
            continue
        todo.append(s)
    visited.add(t)


print("Part 1:",len(visited)*(len(links)-len((visited))))
print("Part 1:",len(visited), len(links))