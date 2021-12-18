import sys


def to_int(n):
    if n.isdecimal():
        return int(n)
    return n


def parse_str(s):
    return list(map(to_int, list(s)))


def explode(st):
    depth = 0
    for i, s in enumerate(st):
        if s == "[":
            depth += 1
        if s == "]":
            depth -= 1
        if depth < 5:
            continue
        lv = st[i + 1]
        rv = st[i + 3]
        for j in range(i - 1, -1, -1):
            if type(st[j]) is int:
                st[j] += lv
                break
        for j in range(i + 6, len(st)):
            if type(st[j]) is int:
                st[j] += rv
                break
        out = st[:i] + [0] + st[i + 5 :]
        return out, False
    return st, True


def split(st):
    for i, s in enumerate(st):
        if type(s) is int and s >= 10:
            out = st[:i]
            out += ["[", s // 2, ",", (s + 1) // 2, "]"]
            out += st[i + 1 :]
            return out, False
    return st, True


def reduc_step(s):
    s, noop = explode(s)
    if noop == False:
        return s, noop
    s, noop = split(s)
    if noop == False:
        return s, noop
    return s, True


def reduc(s):
    while True:
        s, noop = reduc_step(s)
        if noop:
            return s


def sum_pair(a, b):
    s = ["["] + a + [","] + b + ["]"]
    return reduc(s)


def calc_list(pair):
    if type(pair) is not list:
        return pair
    return 3 * calc_list(pair[0]) + 2 * calc_list(pair[1])


def debug(pair):
    return "".join(list(map(str, pair)))


def calc(pair):
    pair = eval(debug(pair))
    return calc_list(pair)


maxv = 0
lines = sys.stdin.readlines()
for i in range(len(lines)):
    a = parse_str(lines[i].strip())
    for j in range(len(lines)):
        if i == j:
            continue
        b = parse_str(lines[j].strip())
        c = sum_pair(a, b)
        maxv = max(maxv, calc(c))
print(maxv)
