def parse_input():
    # Parse data from txt file
    total_arr = []

    with open("Inputs/day_2_input.txt") as input_file:
        for line in input_file:
            total_arr.append(line)

    return total_arr


def part_1():
    ins = parse_input()
    horizontal = 0
    vertical = 0
    for i in ins:
        x = i.split(" ")
        if x[0] == "up":
            vertical -= int(x[1])
        elif x[0] == "down":
            vertical += int(x[1])
        elif x[0] == "forward":
            horizontal += int(x[1])

    print("The final result for Part 1 is: " + str(horizontal * vertical))


def part_2():
    ins = parse_input()
    horizontal = 0
    vertical = 0
    aim = 0

    for i in ins:
        x = i.split(" ")
        if x[0] == "up":
            aim -= int(x[1])
        elif x[0] == "down":
            aim += int(x[1])
        elif x[0] == "forward":
            horizontal += int(x[1])
            vertical += aim * int(x[1])

    print("The final result for Part 2 is: " + str(horizontal * vertical))


if __name__ == "__main__":
    part_1()
    part_2()
