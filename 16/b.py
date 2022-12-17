from collections import namedtuple
import itertools

Valve = namedtuple("Valve", ["name", "flow", "tunnels"])
World = namedtuple("World", ["visited", "unvisited", "busy"])


caves = {}
for line in open("16/sample").readlines():
    [left, right] = line.strip().split(";")
    name = left[6:8]
    flow = int(left[23:])
    tunnels = [text[-2:] for text in right.split(", ")]

    node = Valve(name, flow, tunnels)
    caves[node.name] = node


# Make this a faster diffusion algo
def shortest_path(visited, destination):
    position = visited[-1]
    if position == destination:
        return visited

    unexplored = [name for name in caves[position].tunnels if name not in visited]
    attempts = [shortest_path(visited + [move], destination) for move in unexplored]
    paths = sorted(
        [attempt for attempt in attempts if attempt is not None],
        key=len,
    )

    if len(paths):
        return paths[0]


# Lookup table for shortest distances
def get_distances_table(valves):
    distances = {}
    for source in valves:
        for destination in valves:
            # FIXME: test for symmetrical
            distance = len(
                shortest_path(
                    [source],
                    destination,
                )
            )
            distances[(source, destination)] = distance
            # print(f"{distance: 3d}", end="")
        # print("")

    return distances


def best_score(names, remaining):
    return sum([caves[name].flow * remaining for name in names])


def score(paths):
    return sum(
        [
            sum([remaining * caves[name].flow for (name, remaining) in path])
            for path in paths
        ]
    )


flowing = [valve for valve in caves if caves[valve].flow > 0]
distances = get_distances_table(flowing)


def tick(worlds, remaining):
    print(f"{remaining} - {len(worlds)}")
    new_worlds = []
    max_score = 0

    for world in worlds:
        (visited, unvisited, busy) = world

        new_busy = [business - 1 for business in busy]
        explorers = [i for (i, business) in enumerate(new_busy) if business == 0]

        if len(explorers):
            decisions = min(len(unvisited), len(explorers))
            for destinations in itertools.permutations(unvisited, decisions):
                new_visited = visited.copy()
                new_unvisited = [name for name in unvisited if name not in destinations]
                updated_busy = new_busy.copy()

                for (i, explorer) in enumerate(explorers[:decisions]):
                    last = visited[explorer][-1][0]
                    destination = destinations[i]
                    distance = distances[(last, destination)]
                    # if distance < remaining and score > max_score:
                    #     new_visited[i] = visited[i] + distances

                    new_visited[explorer] = visited[explorer] + [
                        (
                            destination,
                            remaining - distance - 1,
                        )
                    ]

                    updated_busy[explorer] = distance

                new_worlds.append(World(new_visited, new_unvisited, updated_busy))

        else:
            new_worlds.append(World(visited, unvisited, new_busy))

    return new_worlds


total_time = 26
total_explorers = 2

worlds = []
start = "AA"

for names in itertools.permutations(flowing, total_explorers):
    unvisited = [name for name in flowing if name not in names]
    business = [len(shortest_path([start], name)) for name in names]

    visited = [[(name, total_time - business[i])] for (i, name) in enumerate(names)]

    worlds.append(World(visited, unvisited, business))

for time in range(total_time + 1):
    remaining = total_time - time
    worlds = tick(worlds, remaining)

for n in sorted([(score(world.visited), world) for world in worlds])[-5:]:
    print(n)
