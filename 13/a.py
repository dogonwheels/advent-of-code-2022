import json
import common

contents = open("13/input").readlines()
pairs = [
    (json.loads(contents[i].strip()), json.loads(contents[i + 1].strip()))
    for i in range(0, len(contents), 3)
]

print(sum([i + 1 for (i, pair) in enumerate(pairs) if common.in_order(*pair)]))
