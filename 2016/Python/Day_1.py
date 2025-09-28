def parse_input():
    with open("Inputs/day_1_input.txt") as input_file:
        for line in input_file:
           splitter = line.split(", ")

           #Remove newline from the splitter
           splitter[len(splitter)-1] = splitter[len(splitter)-1].replace("\n", "") 

    return splitter

def part_1(list_1):
    loc = [0, 0]

    #0 = N, 1 = E, 2 = S, 3 = W
    heading = 0

    for i in list_1:
        #Parse instruction
        dir_move = i[0]
        num_move = int(i[1:])

        #Change heading
        if dir_move == "R":
            heading += 1
        else:
            heading -= 1

        #Check for wrap around
        if heading < 0:
            heading = 3
        elif heading > 3:
            heading = 0

        #Move
        if heading == 0:
            loc[0] = loc[0] + num_move
        elif heading == 1:
            loc[1] = loc[1] + num_move
        elif heading == 2:
            loc[0] = loc[0] -  num_move
        elif heading == 3:
            loc[1] = loc[1] - num_move

    return abs(loc[0]) + abs(loc[1])


def part_2(list_1):
    loc = [0, 0]
    loc_mem = []

    #0 = N, 1 = E, 2 = S, 3 = W
    heading = 0

    for i in list_1:
        #Parse instruction
        dir_move = i[0]
        num_move = int(i[1:])

        #Change heading
        if dir_move == "R":
            heading += 1
        else:
            heading -= 1

        #Check for wrap around
        if heading < 0:
            heading = 3
        elif heading > 3:
            heading = 0

        #Move
        for j in range(0,num_move):
            if heading == 0:
                loc[0] = loc[0] + 1
            elif heading == 1:
                loc[1] = loc[1] + 1
            elif heading == 2:
                loc[0] = loc[0] -  1
            elif heading == 3:
                loc[1] = loc[1] - 1

            if loc in loc_mem:
                return abs(loc[0]) + abs(loc[1])
            else:
                loc_mem.append(loc.copy())

    print("Couldn't find it...")
    return 0

if __name__ == '__main__':
    # Variables
    list_1 = []

    list_1 = parse_input()

    print("Total Distance: " + str(part_1(list_1)))
    print("Total Distance: " + str(part_2(list_1)))
