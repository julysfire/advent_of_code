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

        surface_area = (2* l * w) + (2 * w * h) + (2 * h * l)

        slack = min(l*w,w*h,l*h)

        total_dims = total_dims + surface_area + slack
    return total_dims

def part_2(list_1):
    pass

if __name__ == '__main__':
    # Variables
    list_1 = []

    list_1 = parse_input()

    print("Total Square Area: " + str(part_1(list_1)))
    print(": " + str(part_2(list_1)))
