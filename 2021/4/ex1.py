import sys

L = 5


def new_val(v):
    return [int(v), False]


def parse_ticket(lines):
    ticket = []
    for l in lines:
        ticket.append(list(map(new_val, l.split())))

    return ticket


def find(t, n):
    for l in range(len(t)):
        for v in range(len(t[l])):
            if t[l][v][0] == n:
                return l, v
    return None


def mark(t, n):
    p = find(t, n)
    if not p:
        return False

    t[p[0]][p[1]][1] = True

    s = 0
    for l in t[p[0]]:
        if l[1]:
            s += 1
    if s == len(t):
        return True

    s = 0
    for l in t:
        if l[p[1]][1]:
            s += 1
    if s == len(t):
        return True

    return False


def calc_value(t):
    s = 0
    for l in t:
        for v in l:
            if not v[1]:
                s += v[0]
    return s


lines = sys.stdin.readlines()

numbers = list(map(int, lines[0].split(",")))

lines = lines[1:]
tickets = []
for i in range(len(lines)//(L+1)):
    tickets.append((parse_ticket(lines[i*(L+1) + 1:(i+1) * (L+1)])))


for n in numbers:
    for t in tickets:
        if mark(t, n):
            print(calc_value(t) * n)
            sys.exit(0)
