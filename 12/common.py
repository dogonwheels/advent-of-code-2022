def parse_heights(filename):
    heights = {}

    rows = open(filename).readlines()
    for (y, row) in enumerate(rows):
        for (x, height) in enumerate(row.strip()):
            if height == "S":
                start = (x, y)
                heights[start] = 1
            elif height == "E":
                end = (x, y)
                heights[end] = 27
            else:
                heights[(x, y)] = ord(height) - 96

    return heights, start, end


directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def climb(heights, start, is_end, gradient):
    visited = {}
    seeds = [start]

    while len(seeds):
        position = seeds.pop()

        if is_end(position):
            path = [position]
            while start not in path:
                path.append(visited[path[-1]])

            return list(reversed(path))

        neighbors = [add(direction, position) for direction in directions]
        unvisited = [neighbor for neighbor in neighbors if neighbor not in visited]
        traversable = [
            neighbor
            for neighbor in unvisited
            if neighbor in heights
            and gradient(position, neighbor)
            and neighbor not in seeds
        ]

        for neighbor in traversable:
            visited[neighbor] = position
            seeds.insert(0, neighbor)
