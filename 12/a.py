from common import parse_heights, climb


def uphill(start, end):
    return heights[end] - heights[start] <= 1


heights, start, end = parse_heights("12/input")
print(len(climb(heights, start, lambda p: p == end, uphill)) - 1)
