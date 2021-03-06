import sys
from functools import reduce
import copy

# from https://fangya.medium.com/chinese-remainder-theorem-with-python-a483de81fbb8


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i)*p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def find_val_fast_chinesse(buses):
    n = list()
    a = list()
    for b in buses:
        n.append(b[0])
        a.append((b[1] * -1) % b[0])
    return int(chinese_remainder(n, a))


def find_pair(a, b):
    # print(a,b)
    step = a[0]
    n = a[1]
    while (n % b[0]) != b[1]:
        n += step

    # print(n)
    r1 = n
    r0 = a[0] * b[0]

    return [r0, r1]


def find_val_fast_ricardo(buses_in):
    buses = copy.deepcopy(buses_in)
    for i in range(len(buses)):
        buses[i][1] = (buses[i][1] * -1) % buses[i][0]

    a = buses[0]
    for b in buses[1:]:
        # print(a,b)
        a = find_pair(a, b)
    return a[1]


def find_val_slow(buses):
    step = 1
    for b in buses:
        if b[1] == 0 and b[0] > step:
            step = b[0]

    val = 0
    while True:
        found = True
        for b in buses:
            if ((val + b[1]) % b[0]) != 0:
                found = False
                break
        if found:
            return val
        val += step


start = int(sys.stdin.readline())
for l in sys.stdin.readlines():
    all_buses = l.split(",")

    offset = 0
    buses = list()
    for b in all_buses:
        if b[0] != "x":
            buses.append([int(b), offset])
        offset += 1
    print(buses)
    print(find_val_fast_chinesse(buses))
    print(find_val_fast_ricardo(buses))
    # print(find_val_slow(buses))
