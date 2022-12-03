import sys


def to_val(letter):
    if ord(letter) >= ord("a"):
        return ord(letter) - ord("a") + 1
    return ord(letter) - ord("A") + 27


output = 0
for l in sys.stdin.readlines():
    left = l[: len(l) // 2]
    right = l[len(l) // 2 :]
    common = set(left) & set(right)
    output += sum(map(to_val, common))

print(output)
