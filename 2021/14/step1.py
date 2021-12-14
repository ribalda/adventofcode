import sys
from collections import Counter


def process_chain(rules, chain):
    out = ""
    for i in range(len(chain)-1):
        out += rules[chain[i:i+2]]
    out += chain[-1]
    return out


lines = sys.stdin.readlines()

chain = lines[0].strip()

rules = dict()
for l in lines[2:]:
    left, right = l.strip().split(" -> ")
    rules[left] = left[0] + right

for i in range(10):
    chain = process_chain(rules, chain)

c = Counter(chain)
print(c[max(c, key=c.get)]-c[min(c, key=c.get)])
