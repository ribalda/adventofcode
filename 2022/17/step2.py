import sys

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
    return int(max([a.real for a in mapa]))


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


def find_sub_list(big, index, small):
    for i in index[small[0]]:
        if i + len(small) == len(big):
            continue
        if big[i : i + len(small)] == small:
            return i
    return -1


mapa = dict()
for i in range(MAX_WIDTH):
    mapa[complex(0, i)] = "-"
p = 0
p_offset = calc_new_piece_offset(mapa)

movs = sys.stdin.readline()
if movs[-1] == "\n":
    movs = movs[:-1]

turn = 0
completed_pieces = 0
last_offset = p_offset
movements = []
heights = []
movement_index = dict()

MAX_PIECES = 1000000000000
CYCLE_CMP = 8
extra_height = 0
while completed_pieces < MAX_PIECES:

    m = movs[turn % len(movs)]
    if m == "<":
        new_offset = p_offset - 1j
    elif m == ">":
        new_offset = p_offset + 1j

    turn += 1
    if not wall_colision(p, new_offset) and not piece_collision(mapa, p, new_offset):
        p_offset = new_offset

    new_offset = p_offset - 1
    if piece_collision(mapa, p, new_offset):
        save_piece(mapa, p, p_offset)
        p = (p + 1) % len(pieces)
        piece_tavel = new_offset - last_offset
        last_offset = new_offset
        p_offset = calc_new_piece_offset(mapa)
        completed_pieces += 1

        if extra_height == 0:
            heights.append(max_heigth(mapa))
            movement = piece_tavel, p
            movements.append(movement)
            if movement not in movement_index:
                movement_index[movement] = []
            movement_index[movement].append(len(movements) - 1)
            last_movements = movements[-CYCLE_CMP:]
            idx = find_sub_list(movements, movement_index, last_movements)
            if idx != -1:
                cycle_len = completed_pieces - (idx + CYCLE_CMP)
                cycle_height = heights[-1] - heights[-cycle_len - 1]
                left = MAX_PIECES - completed_pieces
                missing_cycles = left // cycle_len
                extra_height = missing_cycles * cycle_height
                missing_offset = left % cycle_len
                extra_height2 = (
                    heights[idx + CYCLE_CMP + missing_offset - 1]
                    - heights[idx + CYCLE_CMP - 1]
                )
                print(max_heigth(mapa) + extra_height + extra_height2)
                sys.exit(0)
    else:
        p_offset = new_offset

print(int(max_heigth(mapa)))
