import sys
import os
import time

MAX_WIDTH = 7
pieces = (
    (0j, 1j, 2j, 3j),
    (1j, 1 + 0j, 1 + 1j, 1 + 2j, 2 + 1j),
    (0j, 1j, 2j, 1 + 2j, 2 + 2j),
    (0j, 1 + 0j, 2 + 0j, 3 + 0j),
    (0j, 1j, 1 + 0j, 1 + 1j),
)
pieces_w = (4, 3, 3, 1, 2)


def max_heigth(mapa):
    return max([a.real for a in mapa])


def calc_new_piece_offset(mapa):
    return max_heigth(mapa) + 4 + 2j


def wall_colision(p, offset):
    if offset.imag < 0:
        return True
    if offset.imag + pieces_w[p] > MAX_WIDTH:
        return True
    return False


def piece_collision(mapa, p, offset):
    for k in pieces[p]:
        if k + offset in mapa:
            return True
    return False


def save_piece(mapa, p, offset):
    for k in pieces[p]:
        mapa[k + offset] = "#"


def print_mapa(mapa_in, p, p_offset):
    os.system("clear")

    max_h = int(max_heigth(mapa_in)+5)
    mapa = mapa_in.copy()

    for k in pieces[p]:
        mapa[k + p_offset] = "@"


    for y in range(max(max_h,60), max(max_h-60,-1), -1):
        print("|", end="")
        for x in range(MAX_WIDTH):
            if complex(y, x) in mapa:
                print(mapa[complex(y, x)], end="")
            else:
                print(".", end="")
        print("|")
    time.sleep(0.05)


mapa = dict()
for i in range(MAX_WIDTH):
    mapa[complex(0, i)] = "-"
p = 0
p_offset = calc_new_piece_offset(mapa)
#print_mapa(mapa, p, p_offset)

movs = sys.stdin.readline()
if movs[-1] == "\n":
    movs = movs[:-1]

turn = 0
completed_pieces = 0
while completed_pieces < 2022:
    
    m = movs[turn % len(movs)]
    if m == "<":
        new_offset = p_offset - 1j
    elif m == ">":
        new_offset = p_offset + 1j

    turn += 1
    if not wall_colision(p, new_offset) and not piece_collision(mapa, p, new_offset):
        p_offset = new_offset

    #print_mapa(mapa, p, p_offset)
    new_offset = p_offset - 1
    if piece_collision(mapa, p, new_offset):
        save_piece(mapa, p, p_offset)
        p = (p + 1) % len(pieces)
        p_offset = calc_new_piece_offset(mapa)
        completed_pieces += 1
    else:
        p_offset = new_offset
    #print_mapa(mapa, p, p_offset)

print(int(max_heigth(mapa)))