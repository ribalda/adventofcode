import sys


def get_diff(nums):
    out = []
    for i, val in enumerate(nums[:-1]):
        out.append(nums[i + 1] - val)
    return tuple(out)


def get_sum_diffs(nums):
    out = nums[-1]
    while nums[-1] != 0:
        nums = get_diff(nums)
        out += nums[-1]
    return out


def get_sum_diff_line(line, reverse):
    line = line.split()
    if reverse:
        line = reversed(line)
    nums = tuple(map(int, line))
    return get_sum_diffs(nums)


lines = sys.stdin.readlines()
part1 = sum(map(lambda x: get_sum_diff_line(x, False), lines))
part2 = sum(map(lambda x: get_sum_diff_line(x, True), lines))

print("Part 1:", part1)
print("Part 1:", part2)
