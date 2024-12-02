import sys


def to_report(line):
    return list(map(int, line.split()))


def report_valid(report):
    diffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]

    direction = list(map(lambda x: x > 0, diffs))
    if any(direction) and not all(direction):
        return False

    good_dis = map(lambda x: abs(x) in (1, 2, 3), diffs)
    return all(good_dis)


def report_valid_minus1(report):
    for i in range(len(report)):
        mini_report = report[:i] + report[i + 1 :]
        if report_valid(mini_report):
            return True

    return False


reports = list(map(to_report, sys.stdin.readlines()))


valids = map(int, map(report_valid, reports))
print("Step 1", sum(valids))

valids = map(int, map(report_valid_minus1, reports))
print("Step 2", sum(valids))
