def parse_input():
    # Parse data from txt file
    with open("Inputs/day_1.txt") as input_file:
        for line in input_file:
            splitter = line.split("\n")

            #Assign to each list
            list_1.append(splitter[0])

    return list_1

def part_1(list_1):
    dial_loc = 50
    zero_count = 0

    for i in list_1:
        mov = i[0]
        num = int(i[1:])

        if mov == "L":
            dial_loc = dial_loc - num
        else:
            dial_loc = dial_loc + num

        #Handle rotations 
        if dial_loc < 0:
            while dial_loc < 0:
                dial_loc += 100
        if dial_loc > 99:
            while dial_loc > 99:
                dial_loc -= 100

        if dial_loc == 0:
            zero_count += 1

    return zero_count

def part_2(list_1):
    dial_loc = 50
    zero_count = 0
    pre_loc = 50

    for i in list_1:
        mov = i[0]
        num = int(i[1:])

        while num > 100:
            zero_count += 1
            num -= 100

        if mov == "L":
            dial_loc = dial_loc - num
        else:
            dial_loc = dial_loc + num

        #Handle rotations 
        if dial_loc < 0:
            while dial_loc < 0:
                dial_loc += 100
                if dial_loc != 0 and pre_loc != 0:
                    zero_count += 1
        if dial_loc > 100:
            while dial_loc > 100:
                dial_loc -= 100
                if dial_loc != 0 and pre_loc != 0:
                    zero_count += 1

        if dial_loc == 0:
            zero_count += 1
        if dial_loc == 100:
            zero_count += 1
            dial_loc = 0
    
        pre_loc = dial_loc


    return zero_count


if __name__ == '__main__':
    # Variables
    list_1 = []

    list_1 = parse_input()

    print("Part 1: " + str(part_1(list_1)))
    print("Part 2: " + str(part_2(list_1)))
