def parse_input():
    fullArray = []

    with open("Inputs/day_2_input.txt") as input_file:
        for line in input_file:
            splitter = line.split("x")
            splitter[2] = splitter[2].replace("\n", "")
            fullArray.append(splitter)
    return fullArray


def part_1(list_1):
    total_dims = 0

    for i in list_1:
        l = int(i[0])
        w = int(i[1])
        h = int(i[2])

        surface_area = (2 * l * w) + (2 * w * h) + (2 * h * l)

        slack = min(l * w, w * h, l * h)

        total_dims = total_dims + surface_area + slack

    return total_dims


def part_2(list_1):
    total_dims = 0

    for i in list_1:
        l = int(i[0])
        w = int(i[1])
        h = int(i[2])

        bow = l * w * h

        prez_dim = [l, w, h]
        prez_dim.sort()

        ribbon = prez_dim[0] + prez_dim[0] + prez_dim[1] + prez_dim[1]

        total_dims = total_dims + bow + ribbon

    return total_dims


if __name__ == "__main__":
    list_1 = []

    list_1 = parse_input()

    print("Total Square Area for Part 1: " + str(part_1(list_1)))
    print("Total Square Area for Part 2: " + str(part_2(list_1)))
