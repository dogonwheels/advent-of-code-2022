import common

elves = common.readCalories("1/input")

totals = list(map(sum, elves))
totals.sort(reverse=True)

print(sum(totals[:3]))
