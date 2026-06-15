def parse_input():
    # Parse data from txt file
    total_arr = []

    with open("Inputs/day_1_input.txt") as input_file:
        for line in input_file:
            total_arr.append(line)

    return total_arr


def part_1():
    depths = parse_input()
    increased = 0

    for i in range(1, len(depths)):
        if int(depths[i]) > int(depths[i - 1]):
            increased += 1

    print("The total increased depths in Part 1 is: " + str(increased))


def part_2():
    depths = parse_input()
    increased = 0
    previous = 0

    for i in range(0, len(depths) - 2, 1):
        slide_window = int(depths[i]) + int(depths[i + 1]) + int(depths[i + 2])
        if previous != 0:
            if slide_window > previous:
                increased += 1

        previous = slide_window

    print("The total increased depths in Part 2 is: " + str(increased))


if __name__ == "__main__":
    part_1()
    part_2()
