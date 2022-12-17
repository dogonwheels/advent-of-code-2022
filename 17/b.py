import itertools


pieces = [
    [0b0011110],
    [0b0001000, 0b0011100, 0b0001000],
    [0b0000100, 0b0000100, 0b0011100],
    [0b0010000, 0b0010000, 0b0010000, 0b0010000],
    [0b0011000, 0b0011000],
]


pieces = [
    [(0, 0), (0, 0), (0, 0), (0, 0)],
    [(1, 1), (0, 2), (1, 1)],
    [(0, 0), (0, 0), (0, 2)],
    [(0, 3)],
    [(0, 1), (0, 1)],
]

NONE = 0
DEBUG = 1
VERBOSE = 2
log_level = DEBUG


def log(string, level=VERBOSE):
    if level <= log_level:
        print(string)


def draw_board(heights):
    top = max(heights)

    for y in range(top, -1, -1):
        for i in range(7):
            print("#" if heights[i] <= y else ".", end="")

    print("-------")


heights = [0] * 7

pieces_to_drop = itertools.cycle(pieces)
directions = open("17/sample").read().strip()
directions_to_move = itertools.cycle(directions)

log_level = DEBUG
