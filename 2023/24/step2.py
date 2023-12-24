import sys
import z3


def get_point(three):
    return tuple(map(int, three.split(", ")))


def get_hail(line):
    hail_speed = line.split(" @ ")
    hail_speed = tuple(map(get_point, hail_speed))
    return hail_speed


lines = sys.stdin.readlines()
hails = list(map(get_hail, lines))

x0 = z3.Int("x0")
y0 = z3.Int("y0")
z0 = z3.Int("z0")
sx = z3.Int("sx")
sy = z3.Int("sy")
sz = z3.Int("sz")

s = z3.Solver()


for i, hail in enumerate(hails):
    t = z3.Int("t_" + str(i))
    s.add(t > 0)
    (h_x0, h_y0, h_z0), (h_sx, h_sy, h_sz) = hail
    s.add((h_x0 + h_sx * t) == (x0 + sx * t))
    s.add((h_y0 + h_sy * t) == (y0 + sy * t))
    s.add((h_z0 + h_sz * t) == (z0 + sz * t))
if not s.check():
    print("Part 2: error")
    sys.exit(0)

model = s.model()
s = 0
for m in [x0, y0, z0]:
    s += model[m].as_long()
print("Part2:", s)
