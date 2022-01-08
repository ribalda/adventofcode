import sys
from collections import deque


def deal_increment(deck_in, n):
    deck_out = [None] * len(deck_in)
    pos = 0
    for d in deck_in:
        deck_out[pos] = d
        pos += n
        pos %= len(deck_in)
    if None in deck_out:
        print("Error")
    return deque(deck_out)


N = 10007
deck = deque(range(N))

lines = sys.stdin.readlines()
for l in lines:
    if l.startswith("cut"):
        n = int(l.split()[1])
        deck.rotate(-n)
        continue
    elif l.startswith("deal into"):
        deck.reverse()
        continue
    elif l.startswith("deal with"):
        n = int(l.split()[-1])
        deck = deal_increment(deck, n)
        continue
    else:
        print(l)

print(deck.index(2019))
