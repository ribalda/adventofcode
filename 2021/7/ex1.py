import sys


def pos_weight(crabs, pos):
    val = 0
    for c in crabs:
        val += abs(c - pos)

    return val


crabs = list(map(int, sys.stdin.readline().split(",")))

minval = None
minpos = 0
for i in range(max(crabs)):
    pos_list = pos_weight(crabs, i)
    if minval == None:
        minval = pos_list
    elif pos_list < minval:
        minval = pos_list
        minpos = i


print(minpos, minval)
