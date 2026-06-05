def parse_input():
    full_split = []
    with open("Inputs/day_2_input.txt") as input_file:
        for line in input_file:
            splitter = line.split("\t")

            # Remove newline from the splitter
            splitter[len(splitter) - 1] = splitter[len(splitter) - 1].replace("\n", "")

            full_split.append(splitter)

    return full_split


def part_1():
    sumr = 0
    nums = parse_input()

    for i in range(len(nums)):
        nums_ss = nums[i]
        nums_ss = [int(string) for string in nums_ss]
        nums_ss.sort()

        sumr += nums_ss[len(nums_ss) - 1] - nums_ss[0]

    print("The checksum for Part 1 is: " + str(sumr))


def part_2():
    sumr = 0
    nums = parse_input()

    for i in range(len(nums)):
        nums_ss = nums[i]
        nums_ss = [int(string) for string in nums_ss]

        breaker = 0

        for j in nums_ss:
            for k in nums_ss:
                if j != k and j % k == 0:
                    sumr += j / k
                    breaker = 1
                    break
            if breaker == 1:
                break

    print("The checksum for Part 2 is: " + str(int(sumr)))


if __name__ == "__main__":
    part_1()
    part_2()
