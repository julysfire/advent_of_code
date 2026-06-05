def parse_input():
    splitter = []
    with open("Inputs/day_2_input.txt") as input_file:
        for line in input_file:
            ltext = line.replace("\n", "")
            ltext = ltext.split(" ")
            splitter.append(ltext)
    return splitter


def day_1():
    # A = ROCK, B = PAPER, C = SCISSORS
    # X = ROCK, Y = PAPER, Z = SCISSORS
    # 1, 2, 3 points
    data = parse_input()
    sumr = 0

    for i in data:
        round_score = 0
        elf_pick = i[0]
        you_pick = i[1]

        # Pick
        if you_pick == "X":
            round_score += 1
        elif you_pick == "Y":
            round_score += 2
        else:
            round_score += 3

        # Game
        if elf_pick == "A":
            if you_pick == "X":
                round_score += 3
            elif you_pick == "Y":
                round_score += 6
        elif elf_pick == "B":
            if you_pick == "Y":
                round_score += 3
            elif you_pick == "Z":
                round_score += 6
        else:
            if you_pick == "Z":
                round_score += 3
            elif you_pick == "X":
                round_score += 6

        sumr += round_score

    print("The total score for Part 1: " + str(sumr))


def day_2():
    # A = ROCK, B = PAPER, C = SCISSORS
    # X = ROCK, Y = PAPER, Z = SCISSORS
    # 1, 2, 3 points
    data = parse_input()
    sumr = 0

    for i in data:
        round_score = 0
        elf_pick = i[0]
        you_pick = i[1]

        # Need to lose
        if you_pick == "X":
            if elf_pick == "A":
                round_score += 3
            elif elf_pick == "B":
                round_score += 1
            else:
                round_score += 2
        # Need to draw
        elif you_pick == "Y":
            if elf_pick == "A":
                round_score += 4
            elif elf_pick == "B":
                round_score += 5
            else:
                round_score += 6
        # Need to win
        else:
            if elf_pick == "A":
                round_score += 8
            elif elf_pick == "B":
                round_score += 9
            else:
                round_score += 7

        sumr += round_score

    print("The total score for Part 2: " + str(sumr))


if __name__ == "__main__":
    day_1()
    day_2()
