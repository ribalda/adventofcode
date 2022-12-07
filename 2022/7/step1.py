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


small_dir_sum = 0


def calc_small_dir_sum(d):
    global small_dir_sum
    out = 0

    for f in d:
        if f == "..":
            continue
        if type(d[f]) is dict:
            out += calc_small_dir_sum(d[f])
        else:
            out += d[f]

    if out <= 100000:
        small_dir_sum += out

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

calc_small_dir_sum(root)
print(small_dir_sum)
