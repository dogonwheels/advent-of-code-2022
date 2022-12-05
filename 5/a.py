import common

instructions = open("5/input").readlines()

stacks = common.parse_stacks(instructions)
moves = common.parse_moves(instructions)

for [quantity, source, destination] in moves:
    for transfer in range(quantity):
        stacks[destination].append(stacks[source].pop())

print(common.top_crates(stacks))
