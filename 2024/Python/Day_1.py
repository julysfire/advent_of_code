def parse_input():
    # Parse data from txt file
    with open("inputs\\day_1_input.txt") as input_file:
        for line in input_file:
            splitter = line.split("   ")

            #Remove newline from the split
            splitter[1] = splitter[1].replace("\n", "")

            #Assign to each list
            list_1.append(int(splitter[0]))
            list_2.append(int(splitter[1]))

    return list_1, list_2

def part_1(list_1, list_2):
    total_distance = 0

    # Sort lists
    list_1.sort()
    list_2.sort()

    for i in range(0, len(list_1)):
        total_distance = total_distance + abs(list_1[i] - list_2[i])

    return total_distance

def part_2(list_1, list_2):
    similar_score = 0

    for i in list_1:
        count_from_list = 0
        for j in list_2:
            if i == j:
                count_from_list += 1
        similar_score = similar_score + (count_from_list * i)
    return similar_score


if __name__ == '__main__':
    # Variables
    list_1 = []
    list_2 = []

    list_1, list_2 = parse_input()

    print("Total Distance: " + str(part_1(list_1, list_2)))
    print("Total Similarity Score: " + str(part_2(list_1, list_2)))
