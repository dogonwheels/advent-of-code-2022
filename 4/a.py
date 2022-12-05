def parse_section(section):
    pairs = section.strip().split(",")
    return [[int(value) for value in pair.split("-")] for pair in pairs]


def is_in_range(i, p):
    return i >= p[0] and i <= p[1]


def is_contained(p1, p2):
    first_in_second = is_in_range(p1[0], p2) and is_in_range(p1[1], p2)
    second_in_first = is_in_range(p2[0], p1) and is_in_range(p2[1], p1)
    return first_in_second or second_in_first


sections = [parse_section(section) for section in (open("4/input").readlines())]

print(len([section for section in sections if is_contained(section[0], section[1])]))
