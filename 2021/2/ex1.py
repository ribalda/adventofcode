import sys


def get_mov(name):
    if name == "forward":
        return complex(1, 0)
    elif name == "down":
        return complex(0, 1)
    elif name == "up":
        return complex(0, -1)
    print("Error")
    return None


lines = sys.stdin.readlines()

pos = complex(0, 0)
for l in lines:
    l = l.split()
    pos += int(l[1]) * get_mov(l[0])

print(int(pos.real * pos.imag))
