from common import Survey

survey = Survey("8/input")


def visible(positions):
    visible = []
    maximum = -1
    for position in positions:
        if survey.heights[position] > maximum:
            maximum = survey.heights[position]
            visible.append(position)

    return visible


rows = range(survey.height)
columns = range(survey.width)

never = [survey.get_path((column, 0), (0, 1)) for column in columns]
eat = [survey.get_path((survey.width - 1, row), (-1, 0)) for row in rows]
shredded = [survey.get_path((column, survey.height - 1), (0, -1)) for column in columns]
wheat = [survey.get_path((0, row), (1, 0)) for row in rows]

all_visible_trees = [visible(path) for path in never + eat + shredded + wheat]
distinct_trees = set([tree for path_trees in all_visible_trees for tree in path_trees])

print(len(distinct_trees))
