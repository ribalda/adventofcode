import sys
import itertools

seven_seg = ["abcefg", "cf", "acdeg", "acdfg", "bcdf",
             "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
seven_seg_hash = {s: True for s in seven_seg}


def remap(abc, perm):
    abc = abc.translate(str.maketrans("abcdefg", perm))
    return "".join(sorted(list(abc)))


def find_permutation(ten):
    for p in itertools.permutations(list("abcdefg")):
        p = "".join(p)
        for t in ten:
            t = remap(t, p)
            if t not in seven_seg_hash:
                break
        else:
            return p
    return None


def convert_nums(nums, perm):
    outnum = 0
    for n in nums:
        outnum *= 10
        n = remap(n, perm)
        outnum += seven_seg.index(n)
    return outnum


lines = sys.stdin.readlines()
sum_nums = 0
for l in lines:
    ten, enabled = l.strip().split(" | ")
    perm = find_permutation(ten.split())
    sum_nums += convert_nums(enabled.split(), perm)

print(sum_nums)
