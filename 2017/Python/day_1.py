def parse_input():
    splitter = ""
    with open("Inputs/day_1_input.txt") as input_file:
        for line in input_file:
            splitter = list(line)

            # Remove newline from the splitter
            splitter.pop()

    return splitter


def day_1():
    n_arr = parse_input()
    sumr = 0

    for i in range(len(n_arr)):
        num = int(n_arr[i])
        next_num = int(n_arr[0])

        if i != len(n_arr) - 1:
            next_num = int(n_arr[i + 1])

        if num == next_num:
            sumr += num
    print("The answer to Part 1 is : " + str(sumr))


def day_2():
    n_arr = parse_input()
    sumr = 0
    halfway = len(n_arr) / 2

    for i in range(len(n_arr)):
        num = int(n_arr[i])
        next_pos = int(i + halfway)

        if next_pos >= len(n_arr):
            next_pos = next_pos - len(n_arr)

        next_num = int(n_arr[next_pos])

        if num == next_num:
            sumr += num

    print("The answer to Part 2 is : " + str(sumr))


if __name__ == "__main__":
    day_1()
    day_2()
