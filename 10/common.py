from itertools import accumulate
import operator


def opcode(instruction):
    ops = instruction.split()

    if len(ops) > 1:
        return [0, int(ops[1])]
    else:
        return [0]


def register_over_time(filename):
    instructions = open(filename).readlines()

    registers = [
        register for instruction in instructions for register in opcode(instruction)
    ]

    return list(accumulate(registers, operator.add, initial=1))
