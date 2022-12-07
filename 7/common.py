import itertools


def mkdir(parent):
    return {"parent": parent, "files": {}, "dirs": {}}


def add_size(directory):
    directory["size"] = sum(
        [add_size(child) for child in directory["dirs"].values()]
    ) + sum(directory["files"].values())

    return directory["size"]


def collect_directories(name, directory):
    return [{"name": name, "size": directory["size"]}] + list(
        itertools.chain(
            *[
                collect_directories(name, child)
                for name, child in directory["dirs"].items()
            ]
        )
    )


def get_directories():
    # terminal = open("7/sample").readlines()
    terminal = open("7/input").readlines()

    root = mkdir("")
    location = root

    for line in terminal:
        tokens = line.split()
        if tokens[0] == "$":
            if tokens[1] == "cd":
                if tokens[2] == "/":
                    location = root
                elif tokens[2] == "..":
                    location = location["parent"]
                else:
                    location = location["dirs"][tokens[2]]
            if tokens[1] == "ls":
                continue
        elif tokens[0] == "dir":
            location["dirs"][tokens[1]] = mkdir(location)
        else:
            location["files"][tokens[1]] = int(tokens[0])

    add_size(root)

    return collect_directories("/", root)
