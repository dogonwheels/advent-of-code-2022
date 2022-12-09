def print_board(head, tail):
    for y in range(4, -1, -1):
        line = ""
        for x in range(6):
            if (x, y) == head:
                line = line + "H"
            elif (x, y) == tail:
                line = line + "T"
            else:
                line = line + "."
        print(line)
    print("")


def print_rope(rope):
    for y in range(4, -1, -1):
        line = ""
        for x in range(6):
            if (x, y) in rope:
                index = rope.index((x, y))
                line += str(index) if index > 0 else "H"
            else:
                line = line + "."
        print(line)
    print("")


def print_visits(visits):
    for y in range(4, -1, -1):
        line = ""
        for x in range(6):
            if (x, y) in visits:
                line = line + "#"
            else:
                line = line + "."
        print(line)
    print("")
