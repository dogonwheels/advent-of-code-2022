def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def chase(head, tail):
    dims = range(len(head))
    diff = [head[i] - tail[i] for i in dims]
    mag = [abs(n) for n in diff]
    move = [
        tail[i] + (diff[i] // mag[i] if mag[i] > 1 or sum(mag) > 2 else 0) for i in dims
    ]

    return tuple(move)


if __name__ == "__main__":
    print("(1, 1)? ", chase((2, 1), (1, 1)))
    print("(3, 1)? ", chase((2, 1), (4, 1)))
    print("(2, 1)? ", chase((3, 1), (1, 1)))
    print("(1, 2)? ", chase((1, 3), (1, 1)))
    print("(2, 2)? ", chase((3, 2), (1, 1)))
    print("(2, 2)? ", chase((2, 3), (1, 1)))
