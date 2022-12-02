import sys


def letter_to_num(letter):
    if letter == "A" or letter == "X":
        return 0
    if letter == "B" or letter == "Y":
        return 1
    if letter == "C" or letter == "Z":
        return 2


def calc_win(them, me):
    if them == me:
        return 3
    if me == ((them + 1) % 3):
        return 6
    return 0


points = 0
for line in sys.stdin.readlines():
    them, me = map(letter_to_num, line.split())
    points += calc_win(them, me)
    points += me + 1

print(points)
