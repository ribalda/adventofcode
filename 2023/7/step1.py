import sys
from collections import Counter


def card2point(card):
    ordered = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    ordered.reverse()
    return ordered.index(card)


def lines2game(line):
    card, points = line.split()
    points = int(points)
    card = tuple(map(card2point, list(card)))
    count = list(Counter(card).values())
    count.sort(reverse=True)

    return tuple(count), card, points


lines = sys.stdin.readlines()

games = list(map(lines2game, lines))
games.sort()

print(sum(map(lambda x: (x[0] + 1) * x[1][-1], enumerate(games))))
