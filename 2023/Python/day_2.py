def parse_input():
    splitter = []
    with open("Inputs/day_2_input.txt") as input_file:
        for line in input_file:
            ltext = line.replace("\n", "")
            splitter.append(ltext)
    return splitter


def part_1():
    # Possible: 1 2 red, 13 green, 14 blue
    sumr = 0
    data = parse_input()

    for i in data:
        possible = True

        game_num = int(i[5 : i.find(":")])
        game_data = i[i.find(":") + 1 :]

        game_split = game_data.split("; ")
        for j in game_split:
            cubes = j.split(",")
            for k in cubes:
                if k.find("red") > 0:
                    if int(k.replace("red", "").strip()) > 12:
                        possible = False
                        break
                elif k.find("green") > 0:
                    if int(k.replace("green", "").strip()) > 13:
                        possible = False
                        break
                else:
                    if int(k.replace("blue", "").strip()) > 14:
                        possible = False
                        break
            if possible == False:
                break

        if possible:
            sumr += game_num
    print("The sum of the possible games for Part 1 is: " + str(sumr))


def part_2():
    data = parse_input()
    sumr = 0

    for i in data:
        min_red = 0
        min_green = 0
        min_blue = 0

        game_data = i[i.find(":") + 1 :]

        game_split = game_data.split("; ")
        for j in game_split:
            cubes = j.split(",")
            for k in cubes:
                if k.find("red") > 0:
                    k_i = int(k.replace("red", "").strip())
                    if k_i > min_red:
                        min_red = k_i
                elif k.find("green") > 0:
                    k_i = int(k.replace("green", "").strip())
                    if k_i > min_green:
                        min_green = k_i
                else:
                    k_i = int(k.replace("blue", "").strip())
                    if k_i > min_blue:
                        min_blue = k_i
        sumr += min_red * min_green * min_blue

    print("The power of all the games in Part 2 is: " + str(sumr))


if __name__ == "__main__":
    part_1()
    part_2()
