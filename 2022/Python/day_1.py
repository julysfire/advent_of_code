def parse_input():
    splitter = []
    with open("Inputs/day_1_input.txt") as input_file:
        for line in input_file:
            ltext = line.replace("\n", "")
            splitter.append(ltext)
    return splitter


def part_1():
    data = parse_input()
    fatso = 0
    cals = 0
    elf_counter = 1
    elf_tracker = 0

    for i in data:
        if i == "":
            if cals > fatso:
                fatso = cals
                elf_tracker = elf_counter
            elf_counter += 1
            cals = 0
        else:
            cals += int(i)

    print(
        "Part 1: The fattest elf is Elf # "
        + str(elf_tracker)
        + " at "
        + str(fatso)
        + " calories."
    )


def part_2():
    data = parse_input()
    elfs_data = []
    cals = 0
    elf_counter = 1

    for i in data:
        if i == "":
            elfs_data.append([cals])
            elf_counter += 1
            cals = 0
        else:
            cals += int(i)

    elfs_data.sort(reverse=True)
    three_fat = int(elfs_data[0][0]) + int(elfs_data[1][0]) + int(elfs_data[2][0])

    print("Part 2: The 3 fattest elves calories total: " + str(three_fat))


if __name__ == "__main__":
    part_1()
    part_2()
