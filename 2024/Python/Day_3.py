import re


def part_1():
    total_result = 0
    # Parse data from txt file
    with open("Inputs/day_3_input.txt") as input_file:
        input_text = input_file.read()

    breaker = True

    while breaker:
        mul_index = input_text.find("mul(")
        if mul_index < 0:
            breaker = False
            break

        closing_paren_index = input_text[mul_index:].find(")") + mul_index + 1
        s = input_text[mul_index:closing_paren_index]

        if re.match(r"mul\(([0-9]|[1-9][0-9]|[1-9][0-9][0-9]),([0-9]|[1-9][0-9]|[1-9][0-9][0-9])\)", s):
            x = input_text[mul_index+4:closing_paren_index-1].split(',')
            total_result = total_result + (int(x[0]) * int(x[1]))
        input_text = input_text[mul_index+1:]
    return total_result

def part_2():
    total_result = 0
    # Parse data from txt file
    with open("inputs\\day_3_input.txt") as input_file:
        input_text = input_file.read()

    breaker = True
    do_dont_switch = True

    while breaker:
        mul_index = input_text.find("mul(")
        do_index = input_text.find("do")
        dont_index = input_text.find("don't")

        if mul_index < 0:
            breaker = False
            break

        if do_index == -1:
            do_index = 99999
        if dont_index == -1:
            dont_index = 99999

        if mul_index < do_index and mul_index < dont_index:
            if do_dont_switch:
                closing_paren_index = input_text[mul_index:].find(")") + mul_index + 1
                s = input_text[mul_index:closing_paren_index]

                if re.match(r"mul\(([0-9]|[1-9][0-9]|[1-9][0-9][0-9]),([0-9]|[1-9][0-9]|[1-9][0-9][0-9])\)", s):
                    x = input_text[mul_index + 4:closing_paren_index - 1].split(',')
                    total_result = total_result + (int(x[0]) * int(x[1]))
                input_text = input_text[mul_index + 1:]
            else:
                input_text = input_text[mul_index + 1:]
        elif do_index < mul_index and do_index < dont_index:
            do_dont_switch = True
            input_text = input_text[do_index + 1:]
        elif dont_index < mul_index and dont_index < do_index or (dont_index == do_index):
            do_dont_switch = False
            input_text = input_text[dont_index + 1:]
    return total_result


if __name__ == '__main__':
    print("Total Result: " + str(part_1()))
    print("Total Result: " + str(part_2()))
