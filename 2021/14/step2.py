import sys
from collections import defaultdict


def process_chain(rules, pairs):
    out = defaultdict(int)
    for p in pairs:
        r = rules[p]
        out[r] += pairs[p]
        r2 = rules[p][1] + p[1]
        out[r2] += pairs[p]
    return out


def chain_to_pairs(s):
    pairs = defaultdict(int)
    for i in range(len(s)-1):
        p = s[i:i+2]
        pairs[p] += 1
    return pairs


def counter(pairs):
    histo = defaultdict(int)
    for p in pairs:
        histo[p[0]] += pairs[p]
    return histo


lines = sys.stdin.readlines()

chain = lines[0].strip()
rules = dict()
for l in lines[2:]:
    left, right = l.strip().split(" -> ")
    rules[left] = left[0] + right

pairs = chain_to_pairs(chain)
for i in range(40):
    pairs = process_chain(rules, pairs)

c = counter(pairs)
c[chain[-1]] += 1
print(c[max(c, key=c.get)]-c[min(c, key=c.get)])
