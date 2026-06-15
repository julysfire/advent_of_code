def parse_input():
    splitter = []
    with open("Inputs/day_5_input.txt") as input_file:
        for line in input_file:
            ltext = line.replace("\n", "")
            splitter.append(ltext)

    # Get crane arrays
    crane_temp = []
    crane = []
    for i in range(0, 8, 1):
        x = splitter[i]
        x = [x[j : j + 4] for j in range(0, len(x), 4)]
        for j in range(len(x)):
            x[j] = x[j].strip()
        crane_temp.append(x)

    for i in range(0, 9, 1):
        c_col = []
        for j in range(0, 8, 1):
            if crane_temp[j][i] != "":
                crane_temp[j][i] = crane_temp[j][i].replace("[", "")
                crane_temp[j][i] = crane_temp[j][i].replace("]", "")
                c_col.append(crane_temp[j][i])
        c_col.reverse()
        crane.append(c_col)

    # Get instructions
    instructs = []
    for i in range(11, len(splitter), 1):
        i_col = splitter[i]
        i_col = i_col.replace("move", "")
        i_col = i_col.replace("from", "")
        i_col = i_col.replace("to", "")
        i_col = i_col.split(" ")
        i_col = [i_col[1], i_col[3], i_col[5]]
        instructs.append(i_col)

    return crane, instructs


def part_1():
    crane, instructs = parse_input()
    final_str = ""

    for i in instructs:
        moves = int(i[0])
        from_col = int(i[1]) - 1
        to_col = int(i[2]) - 1

        for _ in range(moves):
            if len(crane[from_col]) == 0:
                break
            letter = crane[from_col][len(crane[from_col]) - 1]
            crane[to_col].append(letter)
            crane[from_col].pop()

    for i in crane:
        final_str += i[len(i) - 1]

    print("The answer for Part 1 is: " + final_str)

    """
    WPVJGWCTQ wrong
    """


def part_2():
    crane, instructs = parse_input()
    sumr = 0

    print("The answer for Part 2 is: " + str(sumr))


if __name__ == "__main__":
    part_1()
    # part_2()
