use std::fs;

pub fn day_1_main() {
    part_1();
    part_2();
}


pub fn part_1(){
    //Ingest data
    let file_name = "inputs/day_1.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

    //Split by each line
    let parts: Vec<&str> = contents.split("\n").collect();

    let mut dial_loc = 50;
    let mut zero_count = 0;

    for i in 0..parts.len()-1{
        let instruct = parts[i];
        let dir = &instruct[0..1];
        let dir_num = &instruct[1..instruct.len()].parse().unwrap();

        if dir == "L"{
            dial_loc = dial_loc - dir_num;
        }else{
            dial_loc = dial_loc + dir_num;
        }

        //Handle rotations 
        if dial_loc < 0{
            while dial_loc < 0{
                dial_loc += 100
            }
        }
        if dial_loc > 99{
            while dial_loc > 99{
                dial_loc -= 100
            }
        }

        if dial_loc == 0{
            zero_count += 1
        }
    }

    println!("The answer to Part 1 is: {}", zero_count);
}

pub fn part_2(){
    //Ingest data
    let file_name = "inputs/day_1.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

    //Split by each line
    let parts: Vec<&str> = contents.split("\n").collect();

    let mut dial_loc = 50;
    let mut zero_count = 0;
    let mut pre_loc = 50;

    for i in 0..parts.len()-1{
        let instruct = parts[i];
        let dir = &instruct[0..1];
        let mut dir_num: i32 = instruct[1..instruct.len()].parse().unwrap();

        while dir_num >= 100{
            zero_count += 1;
            dir_num -= 100;
        }

        if dir == "L"{
            dial_loc = dial_loc - dir_num;
        }else if dir == "R"{
            dial_loc = dial_loc + dir_num;
        }

        //Handle rotations 
        if dial_loc < 0{
            while dial_loc < 0{
                dial_loc += 100;
                if dial_loc != 0 && pre_loc != 0{
                    zero_count += 1;
                }
            }
        }
        if dial_loc > 100{
            while dial_loc > 100{
                dial_loc -= 100;
                if dial_loc != 0 && pre_loc != 0{
                    zero_count += 1;
                }
            }
        }

        if dial_loc == 0{
            zero_count += 1;
        }
        if dial_loc == 100{
            zero_count += 1;
            dial_loc = 0;
        }

        pre_loc = dial_loc;

    }

    println!("The answer to Part 2 is: {}", zero_count);
}
