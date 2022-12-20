import sys

f0 = list(map(int,sys.stdin.readlines()))

f = [(v,idx) for idx, v in enumerate(f0)]
lenf = len(f)

for i in range(len(f)):
    init_order = [a[1] for a in f]
    idx = init_order.index(i)
    v = f.pop(idx)
    new_idx = (idx + v[0]) % (lenf -1)
    f.insert(new_idx, v)

out = 0
values = [a[0] for a in f]
idx0 = values.index(0)
for i in [1000, 2000, 3000]:
    new_idx = (idx0 + i) % lenf
    print(f[new_idx][0])
    out += f[new_idx][0]

print(out)