rucksacks = open("3/input").readlines()


def common_letter(r1, r2, r3):
    for letter in r1:
        if letter in r2 and letter in r3:
            return letter


def score(letter):
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96


letters = [
    score(
        common_letter(rucksacks[i * 3], rucksacks[(i * 3) + 1], rucksacks[(i * 3) + 2])
    )
    for i in range(int(len(rucksacks) / 3))
]

print(sum(letters))
