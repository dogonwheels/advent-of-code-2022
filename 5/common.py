from itertools import dropwhile, takewhile


def parse_moves(instructions):
    def parse_move(move):
        chunks = move.strip().split(" ")
        quantity = int(chunks[1])
        source = int(chunks[3]) - 1
        destination = int(chunks[5]) - 1

        return [quantity, source, destination]

    return [
        parse_move(move)
        for move in dropwhile(lambda instruction: instruction[0] != "m", instructions)
    ]


def parse_stacks(instructions):
    setup = takewhile(lambda instruction: instruction[1] != "1", instructions)
    stacks = [[] for _ in range(len(instructions[0]) // 4)]

    for level in setup:
        for index, crate in enumerate(level[1::4]):
            if crate.isalpha():
                stacks[index].insert(0, crate)

    return stacks


def top_crates(stacks):
    return "".join([stack[-1] for stack in stacks if len(stack) > 0])
