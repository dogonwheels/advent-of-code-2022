class Survey:
    heights = {}
    width = 0
    height = 0

    def __init__(self, filename):
        survey = [
            [int(height) for height in row.strip()]
            for row in open(filename).readlines()
        ]

        self.width = len(survey[0])
        self.height = len(survey)

        self.heights = {}
        for y, row in enumerate(survey):
            for x, tree in enumerate(row):
                self.heights[(x, y)] = tree

    def move(self, position, direction):
        return (position[0] + direction[0], position[1] + direction[1])

    def in_range(self, position):
        return (
            position[0] >= 0
            and position[1] >= 0
            and position[0] < self.width
            and position[1] < self.height
        )

    def get_path(self, position, direction):
        path = []
        while self.in_range(position):
            path.append(position)
            position = self.move(position, direction)

        return path
