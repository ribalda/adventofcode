import sys


def to_bin(hexs):
    out = ""
    for h in hexs:
        d = int(h, 16)
        out += "{0:b}".format(d).zfill(4)
    return out


def eval_literal(bins, idx):
    out = 0
    i = idx
    while(True):
        out *= 16
        out += int(bins[i+1:i+5], 2)
        if bins[i] == "0":
            return (out, i+5)
        i += 5


def eval_value(bins, idx):
    i = idx

    # version
    i += 3
    type_ = int(bins[i:i+3], 2)
    i += 3

    if type_ == 4:
        return eval_literal(bins, i)

    values = []
    length_type_id = int(bins[i:i+1], 2)
    i += 1
    if length_type_id == 0:  # bits
        lenght = int(bins[i:i+15], 2)
        i += 15
        start_i = i
        while i < (start_i + lenght):
            v, i = eval_value(bins, i)
            values.append(v)
    else:
        n = int(bins[i:i+11], 2)
        i += 11
        for _ in range(n):
            v, i = eval_value(bins, i)
            values.append(v)
    # print(values)
    if type_ == 0:
        return sum(values), i
    if type_ == 1:
        out = 1
        for v in values:
            out *= v
        return out, i
    if type_ == 2:
        return min(values), i
    if type_ == 3:
        return max(values), i
    if type_ == 5:
        return int(values[0] > values[1]), i
    if type_ == 6:
        return int(values[0] < values[1]), i
    if type_ == 7:
        return int(values[0] == values[1]), i
    print("error")


for lines in sys.stdin.readlines():
    binstr = to_bin(lines.strip())
    print(eval_value(binstr, 0)[0])
