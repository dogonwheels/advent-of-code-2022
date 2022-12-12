class Monkey:
    def __init__(self, definition):
        self.items = [int(item) for item in definition[1][18:].split(",")]
        self.op = definition[2][19:].split()
        self.modulo = int(definition[3][21:])
        self.receivers = {True: int(definition[4][29:]), False: int(definition[5][30:])}
        self.inspections = 0

    def operation(self, value):
        a = value if self.op[0] == "old" else int(self.op[0])
        b = value if self.op[2] == "old" else int(self.op[2])

        return a * b if self.op[1] == "*" else a + b

    def inspect(self, monkeys, worry_mitigation):
        while len(self.items):
            new = self.operation(self.items.pop(0))
            new = new % worry_mitigation if worry_mitigation else new // 3
            receiver = self.receivers[new % self.modulo == 0]

            self.inspections += 1

            monkeys[receiver].items.append(new)


def parse_monkeys(filename):
    definitions = open(filename).readlines()
    return [
        Monkey(definitions[start : start + 6])
        for start in range(0, len(definitions), 7)
    ]


def get_monkey_business_after(monkeys, rounds, worry_mitigation):
    for _ in range(rounds):
        for monkey in monkeys:
            monkey.inspect(monkeys, worry_mitigation)

    tops = sorted([monkey.inspections for monkey in monkeys])

    return tops[-1] * tops[-2]
