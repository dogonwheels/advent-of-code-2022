from collections import namedtuple
import itertools

Valve = namedtuple("Valve", ["name", "flow", "tunnels"])

caves = {}
for line in open("16/sample").readlines():
    [left, right] = line.strip().split(";")
    name = left[6:8]
    flow = int(left[23:])
    tunnels = [text[-2:] for text in right.split(", ")]

    node = Valve(name, flow, tunnels)
    caves[node.name] = node


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


to_visit = [valve for valve in caves if caves[valve].flow > 0]
print(to_visit)

distances = {}
for source in to_visit:
    for destination in to_visit:
        distance = len(
            shortest_path(
                [source],
                destination,
            )
        )
        distances[(source, destination)] = distance
        print(f"{distance: 3d}", end="")
    print("")

routes = []


def travel(visited, unvisited):
    (last, remaining) = visited[-1]

    destinations = [(move, distances[(last, move)]) for move in unvisited]
    enough_time = [
        destination for destination in destinations if destination[1] <= remaining
    ]

    if len(enough_time):
        for (move, distance) in enough_time:
            new_unvisited = unvisited.copy()
            new_unvisited.remove(move)
            travel(visited + [(move, remaining - distance)], new_unvisited)
    else:
        routes.append(visited)


start = "AA"
for first in to_visit:
    to_first_valve = len(shortest_path([start], first))
    unvisited = to_visit.copy()
    unvisited.remove(first)
    # print([first, 30 - to_first_valve], unvisited)
    travel([(first, 30 - to_first_valve)], unvisited)


def score(visited):
    return sum([caves[name].flow * remaining for (name, remaining) in visited])


def maximum(unvisited, remaining):
    return sum([caves[name].flow * remaining for name in unvisited])


def score(path):
    return sum([remaining * caves[name].flow for (name, remaining) in path])


print(len(routes))
scored = [score(route) for route in routes]
maximum = max(scored)
max_path = routes[scored.index(maximum)]

print(max_path, maximum)
