import sys


def debug(mapa, lines, cols):
    for i in range(lines):
        out = ""
        for j in range(cols):
            if complex(i, j) in mapa:
                out += "#"
            else:
                out += "."
        print(out)


def do_fold(mapa, fold):
    out = dict()

    for m in mapa:
        if fold[0] == "y":
            if m.real > fold[1]:
                m = complex(-m.real + 2 * fold[1], m.imag)
        else:
            if m.imag > fold[1]:
                m = complex(m.real, -m.imag + 2*fold[1])
        out[m] = True

    return out


lines = sys.stdin.readlines()
mapa = dict()
folds = list()

for l in lines:
    if l[0] == "f":
        l = l.split(" ")[2]
        val = int(l[2:])
        folds.append([l[0], val])
    elif l == "\n":
        continue
    else:
        l = l.split(",")
        val = complex(int(l[1]), int(l[0]))
        mapa[val] = True

print(f"Step1: {len(do_fold(mapa, folds[0]))}")
print("Step2:")
for f in folds:
    mapa = do_fold(mapa, f)
    if f == 0:
        print(f"Step 1: {len(mapa)}")
debug(mapa, 6, 40)
