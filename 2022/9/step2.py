import sys


def follow(head, tail):
    diff = head - tail
    if abs(diff.real) < 2 and abs(diff.imag) < 2:
        return tail
    tail = complex(
        tail.real + min(max(diff.real, -1), 1),
        tail.imag + min(max(diff.imag, -1), 1)
    )
    return tail


knots = [0j] * 10
visited = set()
visited.add(knots[-1])

str2mov = {"R": 1, "L": -1, "U": -1j, "D": +1j}

for l in sys.stdin.readlines():
    mov, count = l.split()
    count = int(count)
    mov = str2mov[mov]
    for i in range(count):
        knots[0] += mov
        for k in range(1, len(knots)):
            knots[k] = follow(knots[k - 1], knots[k])
        visited.add(knots[-1])

print(len(visited))
