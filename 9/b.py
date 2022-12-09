from parse import parse_file
from common import add, chase

rope = [(0, 0) for _ in range(10)]
visits = {rope[-1]}


for (direction, distance) in parse_file("9/input"):
    for _ in range(distance):
        rope[0] = add(rope[0], direction)
        for i in range(len(rope) - 1):
            rope[i + 1] = chase(rope[i], rope[i + 1])

        visits.add(rope[-1])


print(len(visits))
