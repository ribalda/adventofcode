import sys

def kk(a):
    return tuple(map(int, a.split(",")))

l = sys.stdin.readline()
print(sorted(list(map(kk, l.split()))))
print(len(list(map(kk, l.split()))))
