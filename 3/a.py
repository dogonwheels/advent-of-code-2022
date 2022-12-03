rucksacks = open("3/input").readlines()


def common_letter(rucksack):
    midpoint = int(len(rucksack) / 2)
    left = rucksack[:midpoint]
    right = rucksack[midpoint:]

    for letter in left:
        if letter in right:
            return letter


def score(letter):
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96


letters = [score(common_letter(rucksack.strip())) for rucksack in rucksacks]

print(sum(letters))
