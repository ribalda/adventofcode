import sys

lines = sys.stdin.readlines()

pos = complex(0, 0)
aim = complex(1, 0)
for l in lines:
    l = l.split()
    name = l[0]
    if name == "forward":
        pos += int(l[1]) * aim
    elif name == "down":
        aim += int(l[1]) * complex(0, 1)
    elif name == "up":
        aim += int(l[1]) * complex(0, -1)
    else:
        print("Error")

print(int(pos.real * pos.imag))
