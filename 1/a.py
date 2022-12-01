import common

elves = common.readCalories("1/input")

totals = list(map(sum, elves))
print(max(totals))
