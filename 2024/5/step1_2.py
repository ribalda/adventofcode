import sys
from functools import cmp_to_key


def orders2pagemin(orders):
    pagemin = set()
    order = orders.splitlines()
    for order in order:
        a, b = order.split("|")
        pagemin.add((int(a), int(b)))
    return pagemin


def page_cmp(pagemin, x, y):
    if (x, y) in pagemin:
        return -1
    if (y, x) in pagemin:
        return 1
    return 0


orders, updates = sys.stdin.read().split("\n\n")

pagemin = orders2pagemin(orders)

out_1, out_2 = 0, 0
for update in updates.splitlines():
    u = list(map(int, update.split(",")))
    sorted_u = sorted(u, key=cmp_to_key(lambda x, y: page_cmp(pagemin, x, y)))
    if u == sorted_u:
        out_1 += u[len(u) // 2]
    else:
        out_2 += sorted_u[len(u) // 2]
print("Step 1:", out_1)
print("Step 2:", out_2)
