# Abandon hope all ye who enter here
# This is bad, like really really really really really bad
# But it worked so.......

def part_1():
    full_map = parse_input()
    walked_map = full_map
    x_cord = 0
    y_cord = 0
    direction = 0
    # direction_list = ['^','>','v','<']

    for i in range(len(full_map)):
        if '^' in full_map[i]:
            y_cord = i
            x_cord = full_map[i].index('^')
            direction = 0
        elif '>' in full_map[i]:
            y_cord = i
            x_cord = full_map[i].index('>')
            direction = 1
        elif '<' in full_map[i]:
            y_cord = i
            x_cord = full_map[i].index("<")
            direction = 2
        elif 'v' in full_map[i]:
            y_cord = i
            x_cord = full_map[i].index('v')
            direction = 3

    while True:
        old_x = x_cord
        old_y = y_cord
        if direction == 0:
            y_cord -= 1
        elif direction == 1:
            x_cord += 1
        elif direction == 2:
            y_cord += 1
        elif direction == 3:
            x_cord -= 1

        res = check_new_loc(x_cord, y_cord, full_map)

        if res == "blocked":
            x_cord = old_x
            y_cord = old_y

            direction += 1
            if direction == 4:
                direction = 0

        walked_map[old_y][old_x] = 'X'

        if res == "oob":
            break
    return count_walked(walked_map)

def part_2():
    full_map = parse_input()
    starting_x = 0
    starting_y = 0
    direction = 0
    infin_count = 0

    for i in range(len(full_map)):
        if '^' in full_map[i]:
            starting_y = i
            starting_x = full_map[i].index('^')
            direction = 0
        elif '>' in full_map[i]:
            starting_y = i
            starting_x = full_map[i].index('>')
            direction = 1
        elif '<' in full_map[i]:
            starting_y = i
            starting_x = full_map[i].index("<")
            direction = 2
        elif 'v' in full_map[i]:
            starting_y = i
            starting_x = full_map[i].index('v')
            direction = 3

    starting_direction = direction

    for ys in range(len(full_map)):
        for xs in range(len(full_map[ys])):
            infin_flag = False
            x_cord = starting_x
            y_cord = starting_y
            direction = starting_direction

            full_map = reset_map(full_map)

            if full_map[ys][xs] == '.' and not (ys == starting_y and xs == starting_x):
                full_map[ys][xs] = '0'

                while True:
                    old_x = x_cord
                    old_y = y_cord
                    if direction == 0:
                        y_cord -= 1
                    elif direction == 1:
                        x_cord += 1
                    elif direction == 2:
                        y_cord += 1
                    elif direction == 3:
                        x_cord -= 1

                    res = check_new_loc(x_cord, y_cord, full_map)

                    if res == "blocked":
                        x_cord = old_x
                        y_cord = old_y

                        direction += 1
                        if direction == 4:
                            direction = 0

                    if full_map[old_y][old_x] == '.' or full_map[old_y][old_x] == '^' or full_map[old_y][old_x] == '>' or full_map[old_y][old_x] == 'v' or full_map[old_y][old_x] == '<':
                        full_map[old_y][old_x] = 1
                    else:
                        if old_x > -1 and old_y > -1:
                            full_map[old_y][old_x] = int(full_map[old_y][old_x]) + 1

                    if full_map[old_y][old_x] == 50:
                        infin_count += 1
                        infin_flag = True

                    if res == "oob" or infin_flag:
                        break

    return infin_count

def reset_map(full_map):
    for i in range(len(full_map)):
        for j in range(len(full_map[i])):
            if int(full_map[i][j] == full_map[i][j]) and full_map[i][j] != '#':
                full_map[i][j] = '.'
    return full_map

def parse_input():
    map_of_area = []

    with open("inputs\\day_6_input.txt") as input_file:
        for line in input_file:
            pre_split = line.replace('\n', '')
            map_of_area.append(list(pre_split))
    return map_of_area

def count_walked(arr):
    counter = 0

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 'X':
                counter += 1
    return counter

def check_new_loc(x, y, map_of_area):
    if x == -1 or y == -1 or y > len(map_of_area)-1 or x > len(map_of_area[0])-1:
        return "oob"
    else:
        if map_of_area[y][x] == "#" or map_of_area[y][x] == '0':
            return "blocked"
        else:
            return "good"


if __name__ == '__main__':
    print("Total Steps: " + str(part_1()))
    print("Total Infinite Loops " + str(part_2()))


'''

< 1800
'''