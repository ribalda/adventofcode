import sys

N = 119315717514047
#N = 10
offset = 0
increment = 1

def get_inv(b):
    return pow(b, -1, N)

def get_idx(idx, inc):
    idx %= N
    inc = get_inv(inc)
    return (idx * inc) % N

def get_val(o_i, pos):
    offset, increment = o_i
    return get_idx(offset + pos, increment)

def cycle(lines, o_i):
    offset, increment = o_i
    for l in lines:
        offset %=  N
        increment %= N
        if l.startswith("cut"):
            n = int(l.split()[1])
            offset += n
            continue
        elif l.startswith("deal into"):
            offset -= 1
            offset *= -1
            increment *= -1
            continue
        elif l.startswith("deal with"):
            n = int(l.split()[-1])
            offset *= n
            increment *= n
            continue
        else:
            continue
            print(l)
    return (offset, increment)

def speedy_cycle(data_in, operation):
    inc = data_in[1] * operation[1]
    offset = data_in[0] * operation[1] + operation[0]
    return offset % N, inc %N


lines = sys.stdin.readlines()
o_i = cycle(lines, (0,1))
output = (0,1)

steps = 101741582076661
v=1
while True:
    if steps & v:
        output = speedy_cycle(output, o_i)
        steps -= v
        if steps == 0:
            break
    o_i = speedy_cycle(o_i, o_i)
    v *= 2

print(get_val(output, 2020))
sys.exit(0)
