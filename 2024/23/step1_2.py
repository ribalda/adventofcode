import sys


def find_triplets_t(conn):
    out = set()
    for x in conn:
        if not x.startswith("t"):
            continue
        for y in conn[x]:
            for z in conn[y]:
                if x in conn[z]:
                    t = tuple(sorted([x, y, z]))
                    out.add(t)
    return out


def find_friend_group(conn, group):
    out = set()
    for c in conn:
        for g in group:
            if c not in conn[g]:
                break
        else:
            new_group = tuple(sorted(list(group) + [c]))
            out.add(new_group)
    return out


def find_biggest_group(conn, group_in):
    while group_in:
        group_out = set()
        for g in group_in:
            group_out |= find_friend_group(conn, g)
        if len(group_out) == 0:
            return ",".join(group_in.pop())
        group_in = group_out


conn = dict()
pairs = set()
for pair in sys.stdin.readlines():
    a, b = pair.strip().split("-")
    pairs.add((min(a, b), max(a, b)))
    for x, y in (a, b), (b, a):
        if x not in conn:
            conn[x] = set()
        conn[x].add(y)

print("Step 1:", len(find_triplets_t(conn)))
print("Step 2:", find_biggest_group(conn, pairs))
