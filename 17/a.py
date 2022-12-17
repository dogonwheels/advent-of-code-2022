import itertools


pieces = [
    [0b0011110],
    [0b0001000, 0b0011100, 0b0001000],
    [0b0000100, 0b0000100, 0b0011100],
    [0b0010000, 0b0010000, 0b0010000, 0b0010000],
    [0b0011000, 0b0011000],
]

NONE = 0
DEBUG = 1
VERBOSE = 2
log_level = DEBUG


def log(string, level=VERBOSE):
    if level <= log_level:
        print(string)


def top_of(board):
    if 0 in board:
        return board.index(0) - 1
    else:
        return len(board) - 1


def piece_row_for_height(piece, piece_bottom, y):
    return -((y - piece_bottom) - len(piece) + 1)


def draw_board(board, piece=[], piece_bottom=0, log_level=VERBOSE):
    height = max(len(board), piece_bottom + len(piece))

    cell = {
        ("0", "0"): ".",
        ("1", "0"): "#",
        ("0", "1"): "@",
        ("1", "1"): "X",
    }

    for y in range(height - 1, -1, -1):
        terrain = 0
        if y < len(board):
            terrain = board[y]
        terrain_formatted = bin(terrain)[2:].zfill(7)
        piece_formatted = "".zfill(7)

        if piece:
            piece_row = piece_row_for_height(piece, piece_bottom, y)
            if piece_row >= 0 and piece_row < len(piece):
                piece_formatted = bin(piece[piece_row])[2:].zfill(7)

        formatted = "".join(
            [cell[(terrain_formatted[i], piece_formatted[i])] for i in range(7)]
        )

        log(f"{y:3d} {formatted}", log_level)


def move_left(piece):
    if not any([row & 0b1000000 for row in piece]):
        return [row << 1 for row in piece]
    else:
        return piece


def move_right(piece):
    if not any([row & 0b0000001 for row in piece]):
        return [row >> 1 for row in piece]
    else:
        return piece


def can_place(board, piece, piece_bottom):
    return not any(
        [
            board[y] & piece[i]
            for (i, y) in enumerate(
                range(piece_bottom + len(piece) - 1, piece_bottom - 1, -1)
            )
        ]
    )


def drop_piece(board, piece, piece_bottom):
    height = max(len(board), piece_bottom + len(piece))
    gap = height - len(board)
    board.extend([0] * gap)


def place_piece(board, piece, piece_bottom):
    for (i, y) in enumerate(range(piece_bottom + len(piece) - 1, piece_bottom - 1, -1)):
        board[y] = board[y] | piece[i]


board = [0b1111111]

pieces_to_drop = itertools.cycle(pieces)

directions = open("17/input").read().strip()
directions_to_move = itertools.cycle(directions)

log_level = NONE

for drops in range(2022):
    print(drops)

    piece = next(pieces_to_drop)
    piece_bottom = top_of(board) + 4
    log(f"O - {top_of(board)} {piece_bottom}", DEBUG)

    drop_piece(board, piece, piece_bottom)
    draw_board(board, piece, piece_bottom, log_level=DEBUG)

    placed = False
    while not placed:
        gust = next(directions_to_move)

        blown_piece = move_left(piece) if gust == "<" else move_right(piece)

        log(gust)

        if can_place(board, blown_piece, piece_bottom):
            piece = blown_piece

        draw_board(board, piece, piece_bottom)

        if can_place(board, piece, piece_bottom - 1):
            log("V")
            piece_bottom -= 1
            draw_board(board, piece, piece_bottom)
        else:
            log("X")
            place_piece(board, piece, piece_bottom)
            placed = True
            draw_board(board)


print(top_of(board))
