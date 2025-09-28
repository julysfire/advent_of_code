def parse_input():
    fullArray = []
    
    with open("Inputs/day_2_input.txt") as input_file:
        for line in input_file:
           splitter = line.split(", ")

           #Remove newline from the splitter
           splitter[len(splitter)-1] = splitter[len(splitter)-1].replace("\n", "") 
           fullArray.append(splitter.copy())

    return fullArray 

def correct_movements(nloc, checkval):
    if nloc[1] > checkval:
        return False
    if nloc[1] < 0:
        return False
    if nloc[0] > checkval:
        return False
    if nloc[0] < 0:
        return False
    return True 

def part_1(list_1):
    keypad = [[1,2,3], [4,5,6], [7,8,9]]
    code = []
    
    for i in list_1:
        loc = [1, 1]
        x = i[0]
         
        for j in range(0, len(x)):
            y = x[j]

            #Move
            if y == "U":
                if correct_movements([loc[0], loc[1] -1], 2):
                    loc[1] = loc[1] - 1
            elif y == "D":
                if correct_movements([loc[0], loc[1] +1], 2):
                    loc[1] = loc[1] + 1
            elif y == "L":
                if correct_movements([loc[0] - 1, loc[1]], 2):
                    loc[0] = loc[0] - 1 
            elif y == "R":
                if correct_movements([loc[0] + 1, loc[1]], 2):
                    loc[0] = loc[0] + 1 
            
        code.append(keypad[loc[1]][loc[0]])
    return code
        
def part_2(list_1):
    keypad = [['z','z',1,'z','z'],['z',2,3,4,'z'],[5,6,7,8,9],['z','A','B','C','z'],['z', 'z', 'D', 'z', 'z']] 

    code = []
    
    for i in list_1:
        loc = [0, 2]
        x = i[0]
         
        for j in range(0, len(x)):
            y = x[j]

            if y == "U":
                if correct_movements([loc[0], loc[1] -1], 4):
                    loc[1] = loc[1] - 1

                    if keypad[loc[1]][loc[0]] == 'z':
                        loc[1] = loc[1] + 1
            elif y == "D":
                if correct_movements([loc[0], loc[1] +1], 4):
                    loc[1] = loc[1] + 1

                    if keypad[loc[1]][loc[0]] == 'z':
                        loc[1] = loc[1] - 1
            elif y == "L":
                if correct_movements([loc[0] - 1, loc[1]], 4):
                    loc[0] = loc[0] - 1 

                    if keypad[loc[1]][loc[0]] == 'z':
                        loc[0] = loc[0] + 1
            elif y == "R":
                if correct_movements([loc[0] + 1, loc[1]], 4):
                    loc[0] = loc[0] + 1 

                    if keypad[loc[1]][loc[0]] == 'z':
                        loc[0] = loc[0] - 1
        code.append(keypad[loc[1]][loc[0]])
    return code


if __name__ == '__main__':
    # Variables
    list_1 = []

    list_1 = parse_input()

    print("Code for Bathroom: " + str(part_1(list_1)))
    print("Real code for the bathroom: " + str(part_2(list_1)))
