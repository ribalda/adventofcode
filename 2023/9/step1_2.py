import sys


def get_diff(nums):
    out = []
    for i, val in enumerate(nums[:-1]):
        out.append(nums[i + 1] - val)
    return tuple(out)


def get_diffs(nums):
    out = [nums]
    while any(nums):
        nums = get_diff(nums)
        out.append(nums)
    return out


def get_diff_line(line):
    nums = tuple(map(int, line.split()))
    return get_diffs(nums)


def get_last(diffs):
    return sum([x[-1] for x in diffs])


def get_first(diffs):
    out = 0
    firsts = list(reversed([x[0] for x in diffs]))
    for f in firsts:
        out = f - out
    return out


lines = sys.stdin.readlines()
diffs = list(map(get_diff_line, lines))

print("Part 1:", sum(map(get_last, diffs)))
print("Part 2:", sum(map(get_first, diffs)))
