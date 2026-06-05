def parse_input():
    splitter = []
    with open("Inputs/day_3_input.txt") as input_file:
        for line in input_file:
            ltext = line.replace("\n", "")
            splitter.append(ltext)
    return splitter


def day_1():
    data = parse_input()
    sumr = 0
    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in data:
        s1 = list(i[: int(len(i) / 2)])
        s2 = list(i[int(len(i) / 2) :])

        item_match = ""

        for j in s1:
            if j in s2:
                item_match = j
                break

        i_index = alpha_lower.find(item_match)
        if i_index == -1:
            i_index = alpha_upper.find(item_match) + 27
        else:
            i_index += 1

        sumr += i_index

    print("The sum of priorties for Part 1 is: " + str(sumr))


def day_2():
    data = parse_input()
    sumr = 0
    alpha_lower = "abcdefghijklmnopqrstuvwxyz"
    alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # Same as above but read 3 lines at once and treat each as their own (don't split the string)
    for i in range(0, len(data), 3):
        letter = ""
        l_1 = list(data[i])
        l_2 = list(data[i + 1])
        l_3 = list(data[i + 2])

        # Find longest
        if len(l_1) >= len(l_2) and len(l_1) >= len(l_3):
            longest = l_1
        elif len(l_2) > len(l_1) and len(l_2) >= len(l_3):
            longest = l_2
        else:
            longest = l_3

        for j in longest:
            if j in l_1 and j in l_2 and j in l_3:
                letter = j
                break

        i_index = alpha_lower.find(letter)
        if i_index == -1:
            i_index = alpha_upper.find(letter) + 27
        else:
            i_index += 1

        sumr += i_index

    print("The sum of priorties for Part 2 is: " + str(sumr))


if __name__ == "__main__":
    day_1()
    day_2()
