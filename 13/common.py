logging = False


def log(tabs, message):
    if logging:
        print(" " * tabs + message)


def in_order(left, right, depth=0):
    if depth > 10:
        print("Delving too greedily and too deep!")
        return

    log(depth, f"- Compare {left} vs {right}")

    if type(left) is int and type(right) is int:
        if left < right:
            log(depth, "- Left side is smaller, so inputs are in the right order")
            return True
        if right < left:
            log(depth, "- Right side is smaller, so inputs are not in the right order")
            return False
        return

    if type(left) is int:
        log(depth, "- Mixed types; convert left to list and retry comparison")
        left = [left]

    if type(right) is int:
        log(depth, "- Mixed types; convert right to list and retry comparison")
        right = [right]

    for l, r in zip(left, right):
        result = in_order(l, r, depth + 1)

        if result is not None:
            return result

    if len(right) < len(left):
        log(depth, "- Right side is smaller, so inputs are not in the right order")
        return False

    if len(left) < len(right):
        log(depth, "- Left side ran out of items, so inputs are in the right order")
        return True
