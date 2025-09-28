import math

def parse_input():
    pre_split = []
    rules = []
    updates = []

    with open("Inputs/day_5_input.txt") as input_file:
        for line in input_file:
            pre_split.append(line)

    file_split_flag = True
    for line in pre_split:
        line = line.replace('\n', '')

        if file_split_flag:
            if line == "":
                file_split_flag = False
            else:
                line = line.split('|')
                rules.append(line)
        else:
            line = line.split(',')
            updates.append(line)

    return rules, updates

def check_rules(rules, num):
    before_list = []
    for i in rules:
        if i[0] == num:
            before_list.append(i[1])
    return before_list

def part_1():
    good_counter = 0
    adder_counter = 0
    rule_list, update_list = parse_input()

    for up in update_list:
        bad = False

        for i in range(len(up)):
            before_list = check_rules(rule_list, up[i])

            bad = validate(up, before_list, i, False)
            if bad:
                break

        if not bad:
            good_counter += 1
            adder_counter = adder_counter + int(up[math.floor(len(up) / 2)])

    print("Part 1 Good Counter: " + str(good_counter) + "    And Sum from Middle Pages: " + str(adder_counter))
    return adder_counter

def part_2():
    good_counter = 0
    adder_counter = 0
    rule_list, update_list = parse_input()

    for up in update_list:
        bad = False

        for i in range(len(up)):
            before_list = check_rules(rule_list, up[i])

            bad, updated_line = validate(up, before_list, i, True, rule_list)

            if bad:
                break
        if bad:
            good_counter += 1
            adder_counter = adder_counter + int(updated_line[math.floor(len(updated_line) / 2)])

    print("Part 2 Rules that were Bad, now Good Counter: " + str(good_counter) + "    And Sum from Middle Pages: " + str(adder_counter))
    return adder_counter

def validate(up_list, before_list, i, part_2_flag, rule_list=None):
    updated_line = []
    for j in range(0, i):
        if up_list[j] in before_list:
            if part_2_flag:
                updated_line = fix_pages(rule_list, up_list)
                break
            else:
                return True
    if part_2_flag:
        if len(updated_line) > 0:
            return True, updated_line
        else:
            return False, updated_line
    else:
        return False


def fix_pages(rule_list, page_list):
    good_counter = 0

    while True:
        reset_flag = False
        for r in rule_list:
            for i in range(0, len(page_list)):
                if r[0] == page_list[i]:
                    for j in range(0, i):
                        if r[1] == page_list[j]:
                            #Swap
                            swap_1 = page_list[j]
                            swap_2 = page_list[i]
                            page_list[j] = swap_2
                            page_list[i] = swap_1

                            reset_flag = True
                            good_counter = 0
                            break
                if reset_flag:
                    break
            if reset_flag:
                break
            else:
                good_counter += 1
        if good_counter == len(rule_list):
            break
    return page_list


if __name__ == '__main__':
    print("Total Correct Updates: " + str(part_1()))
    print("Total After Updates: " + str(part_2()))
