directions = {"R": (1, 0), "U": (0, 1), "L": (-1, 0), "D": (0, -1)}


def parse_instruction(line):
    [direction, distance] = line.split()
    return (directions[direction], int(distance))


def parse_file(filename):
    return [parse_instruction(line) for line in open(filename).readlines()]
