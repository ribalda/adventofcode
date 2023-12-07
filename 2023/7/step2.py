import sys
from collections import Counter


def card2point(card):
    ordered = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    ordered.reverse()
    return ordered.index(card)


def cards2count(cards):
    count = Counter(cards)
    n_j = count.pop(0, 0)
    if n_j == 5:
        return [5]

    count = list(count.values())
    count.sort(reverse=True)
    count[0] += n_j
    return count


def lines2game(line):
    cards, points = line.split()
    points = int(points)
    cards = tuple(map(card2point, list(cards)))

    return tuple(cards2count(cards)), cards, points


lines = sys.stdin.readlines()

games = list(map(lines2game, lines))
games.sort()

print(sum(map(lambda x: (x[0] + 1) * x[1][-1], enumerate(games))))
