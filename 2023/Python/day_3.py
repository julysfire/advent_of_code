def parse_input():
    splitter = []
    with open("Inputs/day_3_input.txt") as input_file:
        for line in input_file:
            ltext = line.replace("\n", "")
            ltext = list(ltext)
            splitter.append(ltext)
    return splitter


def part_1():
    sumr = 0
    data = parse_input()

    for i in range(len(data)):
        print(data[i])
    print("The sum of the possible games for Part 1 is: " + str(sumr))


def part_2():
    data = parse_input()
    sumr = 0
    print("The power of all the games in Part 2 is: " + str(sumr))


if __name__ == "__main__":
    part_1()
    # part_2()
