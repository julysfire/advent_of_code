def parse_input():
    fullArray = []
    
    with open("Inputs/day_3_input.txt") as input_file:
        for line in input_file:
           splitter = line.split(", ")

           #Remove newline from the splitter
           splitter[len(splitter)-1] = splitter[len(splitter)-1].replace("\n", "") 
           fullArray.append(splitter.copy())

    return fullArray 

def split_and_clean(list):
    #Split list and clean
    x = list[0].split("  ")
    y = [z for z in x if z != '']
    y[0] = y[0].strip()
    y[1] = y[1].strip()
    y[2] = y[2].strip()
    
    return y

def part_1(list_1):
    counter = 0
    
    for i in list_1:
        x = split_and_clean(i)

        if (int(x[0]) + int(x[1])) > int(x[2]) and (int(x[0]) + int(x[2])) > int(x[1]) and (int(x[2]) + int(x[1])) > int(x[0]):
            print(x)
            counter+=1
    return counter

def part_2(list_1):
    counter = 0
    
    #TODO
    for i in list_1:
        x = split_and_clean(i)
    
    return counter

if __name__ == '__main__':
    # Variables
    list_1 = []

    list_1 = parse_input()

    print("Possible Trinagles: " + str(part_1(list_1)))
    print("Real code for the bathroom: " + str(part_2(list_1)))
