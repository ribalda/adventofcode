import sys
from collections import Counter


def find_start(line, L):
    counter = Counter()
    for i in range(len(line)):
        if i > L:
            counter[line[i - L]] -= 1
        counter[line[i]] += 1

        if i < L - 1:
            continue
        if counter.most_common(1)[0][1] == 1:
            return i + 1


for line in sys.stdin.readlines():
    print(find_start(line, 4), find_start(line, 14))
