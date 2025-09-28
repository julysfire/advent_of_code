use std::fs;

pub fn day_1_main(){
    part_1();
    part_2();
}

fn part_1(){
    //Ingest data
    let file_name = "inputs/day_1_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

    let chars: Vec<char> = contents.chars().collect();
    let mut floor_level:i32 = 0;

    for i in 0..chars.len(){
        if chars[i] == '(' { floor_level+=1; } else if chars[i] == ')' { floor_level -= 1; }
    }

    println!("Floor level for Part 1: {}", floor_level);
}

fn part_2(){
    //Ingest data
    let file_name = "inputs/day_1_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

    let chars: Vec<char> = contents.chars().collect();
    let mut floor_level:i32 = 0;

    for i in 0..chars.len(){
        if chars[i] == '(' { floor_level+=1; } else if chars[i] == ')' { floor_level -= 1; }

        if floor_level == -1{
            floor_level = (i as i32) + 1;
            break;
        }
    }

    println!("Character Position for Basement in Part 2: {}", floor_level);
}
