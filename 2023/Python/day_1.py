import re


def parse_input():
    splitter = []
    with open("Inputs/day_1_input.txt") as input_file:
        for line in input_file:
            ltext = line.replace("\n", "")
            splitter.append(ltext)
    return splitter


def part_1():
    data = parse_input()
    sumr = 0

    for i in data:
        num_arr = []
        l_list = list(i)

        for j in l_list:
            if re.search(r"[0-9]", j):
                num_arr.append(j)
        first_num = num_arr[0]
        last_num = num_arr[len(num_arr) - 1]
        sumr += int(first_num + last_num)

    print("The sum for Part 1 is: " + str(sumr))


def part_2():
    data = parse_input()
    sumr = 0

    nums_spelled = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for i in data:
        print("Pre : " + i)
        for x in range(len(nums_spelled)):
            i = i.replace(
                nums_spelled[x],
                (
                    nums_spelled[x][0]
                    + nums[x]
                    + nums_spelled[x][
                        len(nums_spelled[x]) - 1
                    ]  # Need to add first and letter to the replace, fiveeight should be 58, not 5ight
                ),
            )
        print("Post: " + i)

        num_arr = []
        l_list = list(i)

        for j in l_list:
            if re.search(r"[0-9]", j):
                num_arr.append(j)
        first_num = num_arr[0]
        last_num = num_arr[len(num_arr) - 1]
        sumr += int(first_num + last_num)

    print("The sum for Part 2 is: " + str(sumr))


if __name__ == "__main__":
    part_1()
    part_2()
