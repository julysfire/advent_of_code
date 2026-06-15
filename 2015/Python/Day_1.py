def parse_input():
    fullArray = []

    with open("Inputs/day_1_input.txt") as input_file:
        for line in input_file:
            fullArray = list(line)
    return fullArray


def part_1(list_1):
    floor = 0

    for i in list_1:
        if i == "(":
            floor += 1
        elif i == ")":
            floor -= 1

    return floor


def part_2(list_1):
    floor = 0
    counter = 0

    for i in list_1:
        counter += 1
        if i == "(":
            floor += 1
        elif i == ")":
            floor -= 1

        if floor < 0:
            break

    return counter


if __name__ == "__main__":
    list_1 = []

    list_1 = parse_input()

    print("The answer to part 1: " + str(part_1(list_1)))
    print("The answer to part 2: " + str(part_2(list_1)))
