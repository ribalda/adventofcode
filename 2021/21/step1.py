import sys

pos = list()

for line in sys.stdin.readlines():
    pos.append((int(line.split()[4]) - 1) % 10)

score = [0] * len(pos)

end = False
dice = 1
while not end:
    for i, p in enumerate(pos):
        val = dice * 3 + 3
        dice += 3
        pos[i] = (p + val) % 10
        score[i] += pos[i] + 1
        if score[i] >= 1000:
            end = True
            break
    # print("pos", pos, "score", score)

print(min(score) * (dice - 1))
