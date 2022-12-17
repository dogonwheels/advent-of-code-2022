from collections import namedtuple
import re

Sensor = namedtuple("Sensor", ["position", "beacon", "distance"])


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def parse_sensor(line):
    s = re.findall(r"-?\d+", line)
    pos = (int(s[0]), int(s[1]))
    beacon = (int(s[2]), int(s[3]))

    return Sensor(pos, beacon, distance(pos, beacon))


def intersection(sensor, y):
    from_sensor = abs(y - sensor.position[1])
    overlap = sensor.distance - from_sensor
    if overlap >= 0:
        return (sensor.position[0] - overlap, sensor.position[0] + overlap)



# print(sensors[3])

# for i in range(20):
#     print(intersection(sensors[3], i), scanned(sensors[3], i))


# for y in range(9, 12):
#     on_line = set([sensor.beacon for sensor in sensors if sensor.beacon[1] == y])
#     line_scanned = [intersection(sensor, y) for sensor in sensors]

#     empty = set()
#     for scan in [line for line in line_scanned if line is not None]:
#         for x in range(scan[0], scan[1] + 1):
#             empty.add(x)

#     for x in range(-4, 27):
#         if (x, y) in on_line:
#             print("B", end="")
#         elif x in empty:
#             print("#", end="")
#         else:
#             print(".", end="")

#     print(" " + str(len(empty) - len(on_line)))


sensors = [parse_sensor(line) for line in open("15/input").readlines()]

y = 2000000

for sensor in sensors:
    dx = distance(sensor.position, sensor.beacon) - abs(sensor.position[1] - y)

    if dx <= 0:
        continue

    print(sensor.position[0] - dx, sensor.position[0] + dx)

# for sensor in sensors:
#     minimum = sensor.position[1] - sensor.distance
#     maximum = sensor.position[1] + sensor.distance
#     print(sensor, minimum, maximum, y >= minimum and y <= maximum)

beacons = set([sensor.beacon for sensor in sensors if sensor.beacon[1] == y])
intersections = [intersection(sensor, y) for sensor in sensors]

empty = set()
for scan in [line for line in intersections if line is not None]:
    for x in range(scan[0], scan[1] + 1):
        empty.add(x)

print(len(empty) - len(beacons), len(empty))

# for line in intersections:
#     print(line)

# print([line for line in intersections if line is not None])

# for x in range(-4, 27):
#     if (x, y) in on_line:
#         print("B", end="")
#     elif x in empty:
#         print("#", end="")
#     else:
#         print(".", end="")

# print(" " + str(len(empty) - len(on_line)))
