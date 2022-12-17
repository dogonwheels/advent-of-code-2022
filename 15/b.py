from collections import namedtuple
import re
import time

Sensor = namedtuple("Sensor", ["position", "beacon", "distance"])


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def parse_sensor(line):
    s = re.findall(r"-?\d+", line)
    pos = (int(s[0]), int(s[1]))
    beacon = (int(s[2]), int(s[3]))

    return Sensor(pos, beacon, distance(pos, beacon))


start = time.time()

ups = []
downs = []

pos = (5, 3)
beacon = (6, 6)
# sensors = [Sensor(pos, beacon, distance(pos, beacon))]
# sensors = [parse_sensor(line) for line in open("15/sample").readlines()]
sensors = [parse_sensor(line) for line in open("15/input").readlines()]

for sensor in sensors:
    edge = sensor.distance + 1
    left = add(sensor.position, (-edge, 0))
    top = add(sensor.position, (0, -edge))
    right = add(sensor.position, (edge, 0))
    bottom = add(sensor.position, (0, edge))

    ups.extend([(left, top), (bottom, right)])
    downs.extend([(top, right), (left, bottom)])


def get_intersection(up, down):
    (up_start, up_end) = up
    (down_start, down_end) = down

    start_x_diff = down_start[0] - up_start[0]
    down_y_at_up_start = down_start[1] - start_x_diff

    distance = (up_start[1] - down_y_at_up_start) / 2

    if distance != int(distance):
        return

    (ix, iy) = add(up_start, (int(distance), int(-distance)))

    # print(ix, up_start[0], up_end[0])

    up_intersects = ix >= up_start[0] and ix <= up_end[0]
    down_intersects = ix > down_start[0] and ix < down_end[0]

    if up_intersects and down_intersects:
        return (ix, iy)


intersections = set()
for up in ups:
    for down in downs:
        i = get_intersection(up, down)
        if i is not None:
            intersections.add(i)

print(intersections)

# filter if outside area

# intersections.add((14, 11))

# print(downs)
# for y in range(20):
#     for x in range(20):
#         chr = "."

#         for sensor in sensors:
#             if distance((x, y), sensor.position) <= sensor.distance:
#                 chr = "O"

#         for up in ups:
#             if x >= up[0][0] and x <= up[1][0]:
#                 dx = x - up[0][0]
#                 if y == up[0][1] - dx:
#                     chr = "/"

#         for down in downs:
#             if x > down[0][0] and x < down[1][0]:
#                 dx = x - down[0][0]
#                 if y == down[0][1] + dx:
#                     chr = "\\"

#         print(chr, end="")

#     print()

bounds = 4000000
for intersection in intersections:
    ranges = [
        distance(sensor.position, intersection) > sensor.distance for sensor in sensors
    ]
    if (
        all(ranges)
        and intersection[0] >= 0
        and intersection[0] <= bounds
        and intersection[1] >= 0
        and intersection[1] <= bounds
    ):
        print(intersection[0] * 4000000 + intersection[1])

# print(intersection(((0, 3), (3, 0)), ((1, 0), (4, 3))))
# intersection(((1, 4), (4, 1)), ((0, 0), (4, 4)))
end = time.time()

# print the difference between start
# and end time in milli. secs
print("The time of execution of above program is :", (end - start) * 10**3, "ms")
