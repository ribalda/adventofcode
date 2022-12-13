import sys
import functools

# smaller, equal, bigger
# -1 , 0 , 1
def ordered(a, b):
    if len(a) == 0 and len(b) == 0:
        return 0
    if len(a) == 0:
        return -1

    for i in range(len(a)):
        if i >= len(b):
            return 1

        if type(a[i]) is int and type(b[i]) is int:
            if a[i] > b[i]:
                return 1
            if a[i] < b[i]:
                return -1
            continue

        if type(a[i]) is int:
            aa = [a[i]]
        else:
            aa = a[i]

        if type(b[i]) is int:
            bb = [b[i]]
        else:
            bb = b[i]
        ret = ordered(aa, bb)
        if ret != 0:
            return ret

    if len(a) != len(b):
        return -1
    return 0


m2 = [[2]]
m6 = [[6]]
messages = [m2, m6]

for l in sys.stdin.readlines():
    if l == "\n":
        continue
    messages.append(eval(l))

messages = sorted(messages, key=functools.cmp_to_key(ordered))

print((messages.index(m2) + 1) * (messages.index(m6) + 1))
