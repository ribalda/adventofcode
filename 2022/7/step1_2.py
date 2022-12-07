import sys
from pprint import pprint


def make_dir(cwd, name):
    if name in cwd:
        return cwd[name]

    new_dir = dict()
    new_dir[".."] = cwd
    cwd[name] = new_dir


def add_files(cwd, files):
    for f in files:
        size, name = f.split()
        if size == "dir":
            make_dir(cwd, name)
        else:
            cwd[name] = int(size)


def change_dir(cwd, d):
    if d not in cwd:
        make_dir(cwd, d)
    return cwd[d]


def calc_dir_sizes(d, sizes):
    out = 0

    for f in d:
        if f == "..":
            continue
        if type(d[f]) is dict:
            out += calc_dir_sizes(d[f], sizes)
        else:
            out += d[f]

    sizes.append(out)

    return out


commands = sys.stdin.read().split("$ ")[2:]

root = dict()

cwd = root
for c in commands:
    lines = c.splitlines()
    command = lines[0]
    if command == "ls":
        add_files(cwd, lines[1:])
    elif command.startswith("cd"):
        d = command.split()[1]
        cwd = change_dir(cwd, d)
    else:
        print("error" + str(lines))

sizes = []
calc_dir_sizes(root, sizes)
sizes = sorted(sizes)

small_sizes = filter(lambda x: x < 100000, sizes)
print("Step 1:", sum(small_sizes))

free_size = 70000000 - sizes[-1]
remove_size = 30000000 - free_size
sizes = filter(lambda x: x > remove_size, sizes)
print("Step 2:", sorted(sizes)[0])
