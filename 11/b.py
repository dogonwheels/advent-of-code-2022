from functools import reduce
from common import parse_monkeys, get_monkey_business_after

monkeys = parse_monkeys("11/input")
worry_mitigation = reduce(lambda x, y: x * y, [monkey.modulo for monkey in monkeys])

print(get_monkey_business_after(monkeys, 10000, worry_mitigation))
