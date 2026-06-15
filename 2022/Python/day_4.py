def parse_input():
    splitter = []
    with open("Inputs/day_4_input.txt") as input_file:
        for line in input_file:
            ltext = line.replace("\n", "")
            splitter.append(ltext)
    return splitter


def part_1():
    data = parse_input()
    sumr = 0
    for i in data:
        split_e = i.split(",")
        e1 = split_e[0].split("-")
        e2 = split_e[1].split("-")

        e1 = [int(x) for x in e1]
        e2 = [int(x) for x in e2]

        if (e1[0] <= e2[0] and e1[1] >= e2[1]) or (e2[0] <= e1[0] and e2[1] >= e1[1]):
            sumr += 1

    print("The total entirely overlapping assignments for Part 1 is: " + str(sumr))


def part_2():
    data = parse_input()
    sumr = 0
    for i in data:
        split_e = i.split(",")
        e1 = split_e[0].split("-")
        e2 = split_e[1].split("-")

        e1 = [int(x) for x in e1]
        e2 = [int(x) for x in e2]

        if (e1[0] <= e2[0] and e1[1] >= e2[1]) or (e2[0] <= e1[0] and e2[1] >= e1[1]):
            sumr += 1
        elif e1[1] >= e2[0] and e1[1] <= e2[1]:
            sumr += 1
        elif e1[0] >= e2[0] and e1[0] <= e2[1]:
            sumr += 1

    print("The total overlapping assignments for Part 2 is: " + str(sumr))


if __name__ == "__main__":
    part_1()
    part_2()
