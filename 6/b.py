def start_of_message(input):
    look_back = 14
    for i in range(look_back, len(input)):
        if len(set(input[i - look_back : i])) == look_back:
            return i


def check_test_input(index, expected):
    input = open("6/sample_b").readlines()[index].strip()

    assert start_of_message(input) == expected


check_test_input(0, 19)
check_test_input(1, 23)
check_test_input(2, 23)
check_test_input(3, 29)
check_test_input(4, 26)

input = open("6/input").read().strip()
print(start_of_message(input))
