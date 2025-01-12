def part_1():
    total_result = 0
    parsed_data = []
    # Parse data from txt file
    with open("inputs\\day_4_input.txt") as input_file:
        for line in input_file:
            splitter = list(line)
            parsed_data.append(splitter)

    for i in range(len(parsed_data)):
        for j in range(len(parsed_data[i])):
            if parsed_data[i][j] == 'X':
                res = search(parsed_data, i, j)
                if res:
                    total_result += res
    return total_result

def search(parsed_data, y, x):
    true_count = 0
    #Forward
    if x + 3 <= len(parsed_data[y]):
        if parsed_data[y][x+1] == 'M' and parsed_data[y][x+2] == 'A' and parsed_data[y][x+3] == 'S':
            true_count += 1

        #Diags
            #Forward down
        if y + 3 <= len(parsed_data)-1:
            if parsed_data[y + 1][x+1] == 'M' and parsed_data[y + 2][x+2] == 'A' and parsed_data[y + 3][x+3] == 'S':
                true_count += 1
            #Forward Up
        if y - 3 > -1:
            if parsed_data[y - 1][x+1] == 'M' and parsed_data[y - 2][x+2] == 'A' and parsed_data[y - 3][x+3] == 'S':
                true_count += 1

    #Backward
    if x - 3 > -1:
        if parsed_data[y][x-1] == 'M' and parsed_data[y][x-2] == 'A' and parsed_data[y][x-3] == 'S':
            true_count += 1

        # Diags
            #Backward down
        if y + 3 <= len(parsed_data)-1:
            if parsed_data[y+1][x-1] == 'M' and parsed_data[y+2][x-2] == 'A' and parsed_data[y+3][x-3] == 'S':
                true_count += 1
            #Backward up
        if y - 3 > -1:
            if parsed_data[y-1][x-1] == 'M' and parsed_data[y-2][x-2] == 'A' and parsed_data[y-3][x-3] == 'S':
                true_count += 1
    #Up
    if y - 3 > -1:
        if parsed_data[y-1][x] == 'M' and parsed_data[y-2][x] == 'A' and parsed_data[y-3][x] == 'S':
            true_count += 1

    #Down
    if y + 3 <= len(parsed_data)-1:
        if parsed_data[y+1][x] == 'M' and parsed_data[y+2][x] == 'A' and parsed_data[y+3][x] == 'S':
            true_count += 1

    return true_count

def part_2():
    total_result = 0
    parsed_data = []
    # Parse data from txt file
    with open("inputs\\day_4_input.txt") as input_file:
        for line in input_file:
            splitter = list(line)
            parsed_data.append(splitter)

    for i in range(len(parsed_data)):
        for j in range(len(parsed_data[i])):
            if parsed_data[i][j] == 'A':
                res = xmas(parsed_data, i, j)
                if res:
                    total_result += res
    return total_result

def xmas(parsed_data, y, x):
    true_count = 0

    if y - 1 > -1 and y + 1 < len(parsed_data):
        # Check top left and bottom left for M or S
        if x-1 > -1 and x + 1 < len(parsed_data[y])-1:
            #Both Top / Both Bottom
            if parsed_data[y-1][x-1] == "M" and parsed_data[y-1][x+1] == "M" and parsed_data[y+1][x-1] == "S" and parsed_data[y+1][x+1] == "S":
                true_count += 1
            elif parsed_data[y-1][x-1] == "S" and parsed_data[y-1][x+1] == "S" and parsed_data[y+1][x-1] == "M" and parsed_data[y+1][x+1] == "M":
                true_count += 1
            #Both Left / Right
            elif parsed_data[y-1][x-1] == "M" and parsed_data[y-1][x+1] == "S" and parsed_data[y+1][x-1] == "M" and parsed_data[y+1][x+1] == "S":
                true_count += 1
            elif parsed_data[y-1][x-1] == "S" and parsed_data[y-1][x+1] == "M" and parsed_data[y+1][x-1] == "S" and parsed_data[y+1][x+1] == "M":
                true_count += 1
    return true_count


if __name__ == '__main__':
    print("Total XMAS: " + str(part_1()))
    print("Total actual XMAS: " + str(part_2()))
