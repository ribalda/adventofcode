import sys
import itertools

seven_seg = [[1, 1, 1, 0, 1, 1, 1], [0, 0, 1, 0, 0, 1, 0], [1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1, 1], [0, 1, 1, 1, 0, 1, 0], [
    1, 1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 0, 1, 0], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1]]
abcdefg = ["a", "b", "c", "d", "e", "f", "g"]


def to_s(abc):
    s = []
    for i in range(len(abcdefg)):
        if abcdefg[i] in abc:
            s.append(1)
        else:
            s.append(0)
    return s


def remap(abc, perm):
    out = [0] * 7
    for i in range(len(abc)):
        if abc[i]:
            out[perm[i]] = 1
    return out


def find_map(ten):
    for p in itertools.permutations(list(range(7))):
        new_ten = []
        for t in ten:
            new_ten.append(remap(t, p))

        found = True
        for n in new_ten:
            if n not in seven_seg:
                found = False
                break

        if found:
            return p
    return None


def convert_nums(nums):
    outnum = ""
    for e in nums:
        e = remap(e, perm)
        for i in range(len(seven_seg)):
            if e == seven_seg[i]:
                outnum += str(i)
                continue
    return int(outnum)


lines = sys.stdin.readlines()
sum_nums = 0
for l in lines:
    ten, enabled = l.strip().split(" | ")
    ten = list(map(to_s, ten.split()))
    enabled = list(map(to_s, enabled.split()))
    perm = find_map(ten)
    sum_nums += convert_nums(enabled)

print(sum_nums)
