def day_2(part_2_opt):
    good_reports = 0

    # Parse data from txt file
    with open("inputs\\day_2_input.txt") as input_file:
        for line in input_file:
            splitter = line.split(" ")

            #Remove newline from the split
            splitter[len(splitter)-1] = splitter[len(splitter)-1].replace("\n", "")

            #Convert to int
            splitter = [int(x) for x in splitter]

            valid_res = test_for_valid(splitter)
            if valid_res:
                good_reports += 1
            elif valid_res is False and part_2_opt:
                # Test with dropping 1 record
                for i in range(0, len(splitter)):
                    removed = splitter.pop(i)

                    valid_res_2 = test_for_valid(splitter)

                    if valid_res_2:
                        good_reports += 1
                        break

                    #Add back
                    splitter.insert(i, removed)
    return good_reports


def test_for_valid(arr):
    if arr[0] > arr[1]:
        asc_desc = "desc"
    elif arr[0] < arr[1]:
        asc_desc = "asc"
    else:
        asc_desc = "bad"

    if asc_desc != "bad":
        for i in range(len(arr) - 1):
            if asc_desc == "asc":
                if (arr[i + 1] >= (arr[i] + 1)) and (arr[i + 1] <= (arr[i] + 3)):
                    pass
                else:
                    asc_desc = "bad"
            else:
                if (arr[i + 1] <= (arr[i] - 1)) and (arr[i + 1] >= (arr[i] - 3)):
                    pass
                else:
                    asc_desc = "bad"
    if asc_desc != "bad":
        return True
    else:
        return False


if __name__ == '__main__':
    print("Number of good reports: " + str(day_2(False)))
    print("Number of good reports within error rate of 1: " + str(day_2(True)))
