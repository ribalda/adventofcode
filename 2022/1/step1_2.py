import sys

inp = sys.stdin.read()[:-1]
blocks = inp.split("\n\n")

elves = []
for b in blocks:
    calories = b.split("\n")
    elf = map(int, b.split("\n"))
    elves.append(elf)

calories = list(map(sum, elves))

print("Step1:", max(calories))

print("Step2:", sum(sorted(calories)[-3:]))
