def start_of_message(input):
    look_back = 4
    for i in range(look_back, len(input)):
        if len(set(input[i - look_back : i])) == look_back:
            return i


def check_test_input(index, expected):
    input = open("6/sample_a").readlines()[index].strip()

    assert start_of_message(input) == expected


check_test_input(0, 5)
check_test_input(1, 6)
check_test_input(2, 10)
check_test_input(3, 11)


input = open("6/input").read().strip()
print(start_of_message(input))
