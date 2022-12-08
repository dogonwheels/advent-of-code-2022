from common import Survey
import math

survey = Survey("8/input")


def view(positions):
    visible = []
    house = survey.heights[positions[0]]
    for position in positions[1:]:
        visible.append(position)
        if survey.heights[position] >= house:
            break

    return visible


def scenic_score(position):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    paths = [survey.get_path(position, direction) for direction in directions]
    scores = [len(view(path)) for path in paths]

    return math.prod(scores)


print(max([scenic_score(position) for position in survey.heights.keys()]))
