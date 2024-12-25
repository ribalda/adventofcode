import sys


def get_lengths(k_l):
    lines = map(lambda x: x.strip(), k_l.splitlines())
    transpose = zip(*lines)
    return ([x.index(x[-1]) for x in transpose])


def valid_keys_locks(keys, locks):
    n = 0
    for key in keys:
        for lock in locks:
            if all(map(lambda x: x[0] <= x[1], zip(key, lock))):
                n += 1
    return n


keys = list()
locks = list()
key_locks = sys.stdin.read().split("\n\n")
for k_l in key_locks:
    lens = get_lengths(k_l)
    if k_l[0][0] == "#":
        keys.append(lens)
    else:
        locks.append(lens)

print("Part 1:", valid_keys_locks(keys, locks))
