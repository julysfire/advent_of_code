use std::fs;

pub fn day_2_main(){
    part_1();
    part_2();
}

fn part_1(){
    //Ingest data
    let file_name = "inputs/day_2_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

    //Split by each line
    let parts: Vec<&str> = contents.split("\n").collect();
    let keypad: [[i32; 3]; 3] = [[1,2,3], [4,5,6], [7,8,9]];

    let mut cords:[i32; 2] = [1, 1];
    let mut final_code = String::new();

    for i in 0..parts.len(){
        let code: Vec<&str> = parts[i].split("").collect();

        for j in 0..code.len(){
            if code[j] == "U"{
                if check_movement([cords[0], cords[1] -1], 2){
                    cords[1] = cords[1] - 1;
                }
            }else if code[j] == "D"{
                if check_movement([cords[0], cords[1] +1], 2){
                    cords[1] = cords[1] + 1;
                }
            }else if code[j] == "L"{
                if check_movement([cords[0] - 1, cords[1]], 2){
                    cords[0] = cords[0] - 1;
                }
            }else if code[j] == "R"{
                if check_movement([cords[0] + 1, cords[1]], 2){
                    cords[0] = cords[0] + 1;
                }
            }
        }

        final_code = final_code + &(keypad[cords[1] as usize][cords[0] as usize]).to_string();
    } 

    println!("Final code in Part 1: {}", final_code);
}

fn part_2(){
    //Ingest data
    let file_name = "inputs/day_2_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

    //Split by each line
    let parts: Vec<&str> = contents.split("\n").collect();
    let keypad: [[&str; 5]; 5] = [["z","z","1","z","z"],["z","2","3","4","z"],["5","6","7","8","9"],["z","A","B","C","z"],["z", "z", "D", "z", "z"]];

    let mut cords:[i32; 2] = [0, 2];
    let mut final_code = String::new();

    for i in 0..parts.len(){
        let code: Vec<&str> = parts[i].split("").collect();

        for j in 0..code.len(){
            if code[j] == "U"{
                if check_movement([cords[0], cords[1] -1], 4){
                    cords[1] = cords[1] - 1;
                    if keypad[cords[1]as usize][cords[0]as usize] == "z"{
                        cords[1] = cords[1] + 1;
                    }
                }
            }else if code[j] == "D"{
                if check_movement([cords[0], cords[1] +1], 4){
                    cords[1] = cords[1] + 1;
                    if keypad[cords[1]as usize][cords[0]as usize] == "z"{
                        cords[1] = cords[1] - 1;
                    }
                }
            }else if code[j] == "L"{
                if check_movement([cords[0] - 1, cords[1]], 4){
                    cords[0] = cords[0] - 1;
                    if keypad[cords[1]as usize][cords[0]as usize] == "z"{
                        cords[0] = cords[0] + 1;
                    }
                }
            }else if code[j] == "R"{
                if check_movement([cords[0] + 1, cords[1]], 4){
                    cords[0] = cords[0] + 1;
                    if keypad[cords[1]as usize][cords[0]as usize] == "z"{
                        cords[0] = cords[0] - 1;
                    }
                }
            }
        }

        final_code = final_code + &(keypad[cords[1] as usize][cords[0] as usize]).to_string();
    } 

    println!("Final code in Part 2: {}", final_code);
}

fn check_movement(loc_val:[i32; 2], check_val: i32) -> bool{
    if loc_val[1] > check_val{
        return false;
    }
    if loc_val[1] < 0{
        return false;
    }
    if loc_val[0] > check_val{
        return false;
    }
    if loc_val[0] < 0{
        return false;
    }
    return true ;
}
