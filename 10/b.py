from common import register_over_time

for index, result in enumerate(register_over_time("10/input")):
    if index % 40 == 0:
        print()

    if index % 40 in [result - 1, result, result + 1]:
        print("#", end="")
    else:
        print(".", end="")
