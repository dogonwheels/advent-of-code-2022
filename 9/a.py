from parse import parse_file
from common import add, chase

head = (0, 0)
tail = head
visits = {tail}

for (direction, distance) in parse_file("9/input"):
    for _ in range(distance):
        head = add(head, direction)
        tail = chase(head, tail)
        visits.add(tail)


print(len(visits))
