import sys


def find_start(line, L):
    for i in range(0, len(line) - L - 1):
        group = line[i : i + L]
        group = sorted(group)
        for k in range(len(group) - 1):
            if group[k] == group[k + 1]:
                break
        else:
            return i + L
    return -1


for line in sys.stdin.readlines():
    print(find_start(line, 4), find_start(line, 14))
