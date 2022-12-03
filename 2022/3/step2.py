import sys


def to_val(letter):
    if letter == "\n":
        return 0
    if ord(letter) >= ord("a"):
        return ord(letter) - ord("a") + 1
    return ord(letter) - ord("A") + 27


output = 0
lines = sys.stdin.readlines()
for i in range(0, len(lines), 3):
    first = lines[i]
    second = lines[i + 1]
    third = lines[i + 2]
    common = set(first) & set(second) & set(third)
    output += sum(map(to_val, common))


print(output)
