from common import parse_heights, climb


def downhill(start, end):
    return heights[end] - heights[start] >= -1


heights, _, start = parse_heights("12/input")
print(len(climb(heights, start, lambda p: heights[p] == 1, downhill)) - 1)
