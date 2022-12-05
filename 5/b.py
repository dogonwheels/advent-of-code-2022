import common

instructions = open("5/input").readlines()

stacks = common.parse_stacks(instructions)
moves = common.parse_moves(instructions)

for [quantity, source, destination] in moves:
    lifted = stacks[source][-quantity:]
    stacks[source] = stacks[source][:-quantity]
    stacks[destination] = stacks[destination] + lifted

print(common.top_crates(stacks))
