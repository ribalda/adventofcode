import sys

head = 0j
tail = 0j
visited = set()
visited.add(tail)

str2mov = {"R": 1, "L": -1, "U": -1j, "D": +1j}

for l in sys.stdin.readlines():
    mov, count = l.split()
    count = int(count)
    mov = str2mov[mov]
    for i in range(count):
        head += mov
        diff = head - tail
        if abs(diff.real) < 2 and abs(diff.imag) < 2:
            continue
        tail = complex(
            tail.real + min(max(diff.real, -1), 1),
            tail.imag + min(max(diff.imag, -1), 1)
        )
        visited.add(tail)

print(len(visited))
