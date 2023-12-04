import sys


def points(wins):
    if wins == 0:
        return 0
    return 1 << wins - 1


def get_win_card(line):
    _, win_card = line.split(": ")
    win, card = win_card.split("|")
    win = set(map(int, win.split()))
    card = set(map(int, card.split()))
    out = len(win & card)
    return out


lines = sys.stdin.readlines()

win = list(map(get_win_card, lines))
print("Step 1:", sum(map(points, win)))


counts = list(map(lambda x: (1, x), win))

for idx, (ni, wini) in enumerate(counts):
    for j in range(idx + 1, idx + 1 + wini):
        nj, winj = counts[j]
        counts[j] = (nj + ni, winj)

print("Step 2:", sum(map(lambda x: x[0], counts)))
