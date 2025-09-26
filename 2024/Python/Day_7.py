import math

def part_1():
    test_nums, number_list = parse_input()

    final_sum = 0

    for i in range(len(test_nums)):

        num_list = number_list[i]
        combinations = int(math.pow(2, len(num_list)-1))-1
        bin_num = bin(combinations)

        for j in range(int(bin_num, 2), -1, -1):
            j_bin = bin(j)
            j_str = str(j_bin[2:])

            if len(j_str) < len(str(bin_num[2:])):
                j_str = ((len(str(bin_num[2:])) - len(j_str)) * '0') + j_str

            #Build eval_str
            eval_str = ""
            test_sum = ""

            for x in range(0, len(num_list)):
                eval_str = eval_str + num_list[x]
                test_sum = eval(str(test_sum) + eval_str)
                eval_str = ""

                if x < len(num_list)-1:
                    if j_str[x] == "1":
                        eval_str = eval_str + "*"
                    else:
                        eval_str = eval_str + "+"

            if test_sum == int(test_nums[i]):
                final_sum = final_sum + int(test_nums[i])
                break
    return final_sum

def part_2():
    test_nums, number_list = parse_input()

    final_sum = 0
    return final_sum

def parse_input():
    test_eq = []
    num_list = []

    with open("inputs\\day_7_input.txt") as input_file:
        for line in input_file:
            pre_split = line.replace('\n', '')
            holder = pre_split.split(":")
            test_eq.append(holder[0])

            holder2 = holder[1].split(' ')
            holder2.pop(0)
            num_list.append(holder2)
    return test_eq, num_list


if __name__ == '__main__':
    #print("Total of Correct Results Sum: " + str(part_1()))
    print("Total actual XMAS: " + str(part_2()))

