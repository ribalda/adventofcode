import sys
import itertools


def calc_dist(i, j):
    s = 0
    for k in range(len(i)):
        s += abs(i[k] - j[k])
    return s


def calc_all_dist(s):
    s["dists"] = []
    for i in s["beacons"]:
        dist = set()
        for j in s["beacons"]:
            dist.add(calc_dist(i, j))
        s["dists"].append(dist)
    return


def parity(sub):
    aux = list(sub)
    n = 0
    for i in range(len(sub)):
        if aux[i] == i + 1:
            continue
        aux[aux.index(i + 1)] = aux[i]
        aux[i] = i + 1
        n += 1
    return n & 1


def last_sign(per, par):
    n = par
    for i in range(len(per) - 1):
        if per[i] < 0:
            n += 1
    return n & 1


def enumerate_ops():
    for p in itertools.permutations([1, 2, 3]):
        par = parity(p)

        for i in range(4):
            p2 = list(p)
            for k in range(2):
                if i & 2 ** k:
                    p2[k] *= -1
            if last_sign(p2, par):
                p2[-1] *= -1
            yield (tuple(p2))


OP_LIST = list(enumerate_ops())


def operate(v, op):
    out = [0, 0, 0]
    for i in range(3):
        out[i] = v[abs(op[i]) - 1]
        if op[i] < 0:
            out[i] *= -1
    return tuple(out)


def tsub(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] - b[i])
    return tuple(c)


def calc_op_offset_pivot(scanA, scanB, i, j):
    distsA = set()
    orig = scanA["beacons"][i]
    for b in scanA["beacons"]:
        distsA.add(tsub(b, orig))

    for o in OP_LIST:
        orig = operate(scanB["beacons"][j], o)
        distsB = set()
        for b in scanB["beacons"]:
            dest = operate(b, o)
            distsB.add(tsub(dest, orig))
        common = distsA & distsB
        if len(common) >= 12:
            return tsub(orig, scanA["beacons"][i]), o
    return None


def calc_operation_offset(scanA, scanB):
    for i, valI in enumerate(scanA["dists"]):
        for j, valJ in enumerate(scanB["dists"]):
            common = valI & valJ
            if len(common) < 12:
                continue
            res = calc_op_offset_pivot(scanA, scanB, i, j)
            if res == None:
                continue
            offset, op = res
            beacons = list()
            for b in scanB["beacons"]:
                b = operate(b, op)
                b = tsub(b, offset)
                beacons.append(b)
            scanB["beacons"] = beacons
            scanB["offset"] = tsub((0, 0, 0), offset)
            return True
    return False


lines = sys.stdin.readlines()
scanners = list()
i = 0
while i < len(lines):
    s = dict()
    s["id"] = int(lines[i].split()[2])
    i += 1
    beacons = []
    while True:
        if i >= len(lines):
            break
        b = lines[i].split(",")
        i += 1
        if len(b) != 3:
            break
        b = tuple(map(int, b))
        beacons.append(b)
    s["beacons"] = beacons
    calc_all_dist(s)
    scanners.append(s)

scanners[0]["offset"] = (0, 0, 0)
todo = [0]
unknown = list(range(1, len(scanners)))
while unknown and todo:
    t = todo[0]
    for s in unknown:
        if calc_operation_offset(scanners[t], scanners[s]):
            todo.append(s)
            unknown.remove(s)
            break
    else:
        todo.pop(0)

beacons = set()
for s in scanners:
    for b in s["beacons"]:
        beacons.add(b)
print("Step1", len(beacons))

max_dist = 0
for s in scanners:
    for t in scanners:
        d = calc_dist(s["offset"], t["offset"])
        max_dist = max(d, max_dist)

print("Step2", max_dist)
