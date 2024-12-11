import sys
from functools import cache


def blink(stone):
    if stone == 0:
        return (1,)
    st_stone = str(stone)
    l_stone = len(st_stone)
    if l_stone % 2 == 0:
        mid = l_stone // 2
        return (int(st_stone[:mid]), int(st_stone[mid:]))
    return (stone * 2024,)


@cache
def blink_n(stone, n_blinks):
    blinked = blink(stone)
    if n_blinks == 1:
        return len(blinked)
    return sum(map(lambda x: blink_n(x, n_blinks - 1), blinked))


def total_stones(stones, n_blinks):
    return sum(map(lambda x: blink_n(x, n_blinks), stones))


stones = list(map(int, sys.stdin.readline().split()))
print("Step 1:", total_stones(stones, 25))

print("Step 2:", total_stones(stones, 75))
