import sys


def next(val):
    val = (val ^ (val * 64)) % 16777216
    val = (val ^ (val // 32)) % 16777216
    val = (val ^ (val * 2048)) % 16777216
    return val


def next_2000(val):
    for _ in range(2000):
        val = next(val)
    return val


def sequences(val):
    out = dict()
    v = [val]
    d = []
    for _ in range(4):
        v.append(next(v[-1]))
        d.append((v[-1] % 10) - (v[-2] % 10))

    for _ in range(2000 - 5):
        seq = tuple(d)
        if seq not in out:
            out[seq] = v[-1] % 10
        v = v[1:] + [next(v[-1])]
        d = d[1:] + [(v[-1] % 10) - (v[-2] % 10)]
    return out


def best_sequence(nums):
    seqs = dict()
    for n in nums:
        seq_n = sequences(n)
        for s in seq_n:
            if s not in seqs:
                seqs[s] = 0
            seqs[s] += seq_n[s]
    return max(seqs.values())


nums = list(map(int, sys.stdin.readlines()))
print("Part 1", sum(map(next_2000, nums)))
print("Part 2", best_sequence(nums))
