terrain = {}
ROCK = "#"
SAND = "O"


def draw_path(path, terrain):
    points = [
        (int(point[0]), int(point[1]))
        for point in [point.split(",") for point in path.strip().split(" -> ")]
    ]

    pos = points[0]
    points.pop(0)
    while len(points):
        terrain[pos] = ROCK

        if pos == points[0]:
            points.pop(0)
        else:
            dx = points[0][0] - pos[0]
            dy = points[0][1] - pos[1]
            m = max(abs(dx), abs(dy))
            pos = (pos[0] + (dx // m), pos[1] + (dy // m))


def print_terrain(terrain, minimum, maximum):
    for y in range(minimum[1], maximum[1] + 1):
        for x in range(minimum[0], maximum[0] + 1):
            if (x, y) in terrain:
                print(terrain[(x, y)], end="")
            else:
                print(".", end="")
        print("")


def fall(terrain, position, the_void):
    if position[1] + 1 == the_void:
        return position

    left = (position[0] - 1, position[1] + 1)
    down = (position[0], position[1] + 1)
    right = (position[0] + 1, position[1] + 1)

    possible = [
        location for location in [down, left, right] if location not in terrain
    ] + [position]

    return possible[0]


paths = open("14/input").readlines()
[draw_path(path, terrain) for path in paths]


spawn = (500, 0)

the_void = max([pos[1] for pos in terrain.keys() if terrain[pos] == ROCK]) + 2
entered_the_void = False

while spawn not in terrain:
    position = spawn
    terrain[position] = SAND
    new_position = fall(terrain, position, the_void)

    while new_position is not position:
        terrain.pop(position)
        position = new_position
        terrain[position] = SAND
        new_position = fall(terrain, position, the_void)

        # print_terrain(terrain, (494, 0), (503, 11))

print(len([pos for (pos, substance) in terrain.items() if substance is SAND]))
