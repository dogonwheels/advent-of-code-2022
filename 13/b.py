from functools import cmp_to_key
import json
import math
import common

contents = open("13/input").readlines()
lines = [json.loads(line.strip()) for line in contents if len(line) > 1]


def compare(left, right):
    result = common.in_order(left, right)
    if result == True:
        return -1
    elif result == False:
        return 1
    else:
        return 0


dividers = [[[2]], [[6]]]
lines.extend(dividers)

result = sorted(lines, key=cmp_to_key(compare))

print(math.prod([result.index(divider) + 1 for divider in dividers]))
