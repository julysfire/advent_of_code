use std::fs;

pub fn day_3_main(){
    part_1();
    part_2();
}

fn part_1(){
    //Ingest data
    let file_name = "inputs/day_3_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

    let parts: Vec<&str> = contents.split("").collect();

    let mut locmem: Vec<[i32; 2]> = Vec::new();
    let mut loc: [i32; 2] = [0, 0];

    for i in 0..parts.len()-2{
        if parts[i] == "^"{
            loc[1] += 1;
        }else if parts[i] == "v"{
            loc[1] -= 1;
        }else if parts[i] == "<"{
            loc[0] -= 1;
        }else if parts[i] == ">"{
            loc[0] += 1;
        }

        if locmem.contains(&loc) == false{
            locmem.push(loc);
        }
    }

    println!("Total Houses seen in Part 1: {}", locmem.len());
}

fn part_2(){
    //Ingest data
    let file_name = "inputs/day_3_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

    let parts: Vec<&str> = contents.split("").collect();

    let mut locmem: Vec<[i32; 2]> = Vec::new();
    let mut loc_santa: [i32; 2] = [0, 0];
    let mut loc_robo_santa: [i32; 2] = [0, 0];
    let mut turn: i32 = 0;

    for i in 0..parts.len()-2{
        if parts[i] == "^"{
            if turn == 0{
                loc_santa[1] += 1
            }else{
                loc_robo_santa[1] += 1;
            }
        }else if parts[i] == "v"{
            if turn == 0{
                loc_santa[1] -= 1;
            }else{
                loc_robo_santa[1] -= 1;
            }
        }else if parts[i] == "<"{
            if turn == 0{
                loc_santa[0] -= 1;
            }else{
                loc_robo_santa[0] -= 1;
            }
        }else if parts[i] == ">"{
            if turn == 0{
                loc_santa[0] += 1;
            }else{
                loc_robo_santa[0] += 1;
            }
        }


        if turn == 0{
            if locmem.contains(&loc_santa) == false{
                locmem.push(loc_santa);
            }
            turn = 1;
        }else{
            if locmem.contains(&loc_robo_santa) == false{
                locmem.push(loc_robo_santa);
            }
            turn = 0;
        }
    }

    println!("Total Houses seen in Part 2: {}", locmem.len());
}
