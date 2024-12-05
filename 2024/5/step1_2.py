import sys
from functools import cmp_to_key


def orders2pagemin(orders):
    pagemin = set()
    order = orders.splitlines()
    for order in order:
        a, b = order.split("|")
        a, b = int(a), int(b)
        pagemin.add((a, b))
    return pagemin


def valid_update(pagemin, update):
    for i, a in enumerate(update):
        for b in update[i + 1 :]:
            if (b, a) in pagemin:
                return False
    return True

def page_cmp(pagemin, x , y):
    if (x,y) in pagemin:
        return -1
    if (y,x) in pagemin:
        return 1
    return 0


orders, updates = sys.stdin.read().split("\n\n")

pagemin = orders2pagemin(orders)

out = 0
unsorted = []
for update in updates.splitlines():
    u = list(map(int, update.split(",")))
    if valid_update(pagemin, u):
        out += u[len(u) // 2]
    else:
        unsorted.append(u) 

print("Step 1:", out)

out = 0
for u in unsorted:
    u = sorted(u, key = cmp_to_key(lambda x,y: page_cmp(pagemin, x, y)))
    out += u[len(u) // 2]
print("Step 2:", out)
