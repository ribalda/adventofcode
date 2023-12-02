import sys


def get_run(runs):
    out = dict()
    for color in runs.split(", "):
        n, c = color.split(" ")
        out[c] = int(n)
    return out


def get_games(line):
    _, runs = line.strip().split(": ")
    return list(map(get_run, runs.split("; ")))


def get_max(game):
    colors = {"red": 0, "green": 0, "blue": 0}
    for run in game:
        for c in run:
            colors[c] = max(colors[c], run[c])
    return colors


def get_power(ma):
    colors = ("red", "green", "blue")
    out = 1
    for c in colors:
        out *= ma[c]
    return out


lines = sys.stdin.readlines()
games = map(get_games, lines)
maxes = list(map(get_max, games))

cubes = {"red": 12, "green": 13, "blue": 14}
step1 = 0
for idx, m in enumerate(maxes):
    for c in cubes:
        if m[c] > cubes[c]:
            break
    else:
        step1 += idx + 1
print("Step1:", step1)

maxes = map(get_power, list(maxes))
step2 = sum(maxes)
print("Step2:", step2)
