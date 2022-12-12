def slope(start, end):
    if start[0] < end[0]:
        return ">"
    elif start[0] > end[0]:
        return "<"
    elif start[1] < end[1]:
        return "V"
    else:
        return "^"


def print_path(heights, path):
    bounds = sorted(heights.keys())[-1]
    for y in range(bounds[1] + 1):
        for x in range(bounds[0] + 1):
            if (x, y) in path:
                i = path.index((x, y))
                if i < len(path) - 1:
                    print(slope(path[i], path[i + 1]), end="")
                else:
                    print("!", end="")
            else:
                print(chr(heights[(x, y)] + 96), end="")
        print("")
