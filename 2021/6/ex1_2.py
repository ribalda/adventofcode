import sys

N = 7

fishes = [0] * (N+2)

fi = list(map(int, sys.stdin.readline().split(",")))
for f in fi:
    fishes[f] += 1

time = 0

for i in range(int((sys.argv[1]))):
    f_0 = fishes[time]
    fishes[time] += fishes[N]
    fishes[N] = fishes[N+1]
    fishes[N+1] = f_0
    time = (time + 1) % N

print(sum(fishes))
