import sys


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


def calc_small_dir_sum(d, sizes):
    global small_dir_sum
    out = 0

    for f in d:
        if f == "..":
            continue
        if type(d[f]) is dict:
            out += calc_small_dir_sum(d[f], sizes)
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
calc_small_dir_sum(root, sizes)
sizes = sorted(sizes)

free_size = 70000000 - sizes[-1]
remove_size = 30000000 - free_size

sizes = filter(lambda x: x > remove_size, sizes)
print(sorted(sizes)[0])
