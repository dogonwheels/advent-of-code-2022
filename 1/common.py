def readCalories(filename):
    lines = open(filename).readlines()

    elves = []
    elf = []
    for line in lines:
        value = line.strip()
        if value.isnumeric():
            elf.append(int(value))
        else:
            elves.append(elf)
            elf = []
    elves.append(elf)

    return elves
