def parse_input():
    fullArray = []

    with open("Inputs/day_3_input.txt") as input_file:
        for line in input_file:
            fullArray = list(line)
    return fullArray


def part_1(list_1):
    loc = [0, 0]
    loc_mem = []

    for i in list_1:
        if i == "^":
            loc[1] += 1
        elif i == "v":
            loc[1] -= 1
        elif i == "<":
            loc[0] -= 1
        elif i == ">":
            loc[0] += 1

        if loc in loc_mem:
            pass
        else:
            loc_mem.append(loc.copy())

    return len(loc_mem) + 1


def part_2(list_1):
    loc_mem = []
    loc_santa = [0, 0]
    loc_robo = [0, 0]
    turn = 0

    for i in range(len(list_1)):
        if list_1[i] == "^":
            if turn == 0:
                loc_santa[1] += 1
            else:
                loc_robo[1] += 1
        elif list_1[i] == "v":
            if turn == 0:
                loc_santa[1] -= 1
            else:
                loc_robo[1] -= 1
        elif list_1[i] == "<":
            if turn == 0:
                loc_santa[0] -= 1
            else:
                loc_robo[0] -= 1
        elif list_1[i] == ">":
            if turn == 0:
                loc_santa[0] += 1
            else:
                loc_robo[0] += 1

        if turn == 0:
            if loc_santa in loc_mem:
                pass
            else:
                loc_mem.append(loc_santa.copy())
            turn = 1
        else:
            if loc_robo in loc_mem:
                pass
            else:
                loc_mem.append(loc_robo.copy())
            turn = 0

    return len(loc_mem)


if __name__ == "__main__":
    list_1 = []

    list_1 = parse_input()

    print("The answer for Part 1: " + str(part_1(list_1)))
    print("The answer for Part 2: " + str(part_2(list_1)))
