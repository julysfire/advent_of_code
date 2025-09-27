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

    //Split by each line
    let parts: Vec<&str> = contents.split(", ").collect();

    let mut loc: [i32; 2] = [0, 0];

    //0 = N, 1 = E, 2 = S, 3 = W
    let mut heading: i32 = 0;

    for i in 0..parts.len(){
        //Parse instruction
        let chars = String::from(parts[i].replace("\n", ""));
        let dir_move = chars.chars().next().map(|c| c.to_string()).unwrap();
        let num_move_str:String = chars.chars().skip(1).collect();
        let num_move: i32 = num_move_str.parse()
            .expect("Not a valid number");

        //Change heading
        if dir_move == "R"{
            heading += 1;
        }else{
            heading -= 1;
        }

        //Check for wrap around
        if heading < 0{
            heading = 3;
        }else if heading > 3{
            heading = 0;
        }

        //Move
        if heading == 0{
            loc[0] = loc[0] + num_move;
        }else if heading == 1{
            loc[1] = loc[1] + num_move;
        }else if heading == 2{
            loc[0] = loc[0] -  num_move;
        }else if heading == 3{
            loc[1] = loc[1] - num_move;
        }
    }

    println!("Total distance moved in Part 1: {}", (loc[0].abs() + loc[1].abs()));
}

fn part_2(){
    //Ingest data
    let file_name = "inputs/day_1_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

    //Split by each line
    let parts: Vec<&str> = contents.split(", ").collect();
    
    let mut locmem: Vec<[i32; 2]> = Vec::new();
    let mut loc: [i32; 2] = [0, 0];

    //0 = N, 1 = E, 2 = S, 3 = W
    let mut heading: i32 = 0;

    for i in 0..parts.len(){
        let mut checker: bool = true;

        //Parse instruction
        let chars = String::from(parts[i].replace("\n", ""));
        let dir_move = chars.chars().next().map(|c| c.to_string()).unwrap();
        let num_move_str:String = chars.chars().skip(1).collect();
        let num_move: i32 = num_move_str.parse()
            .expect("Not a valid number");

        //Change heading
        if dir_move == "R"{
            heading += 1;
        }else{
            heading -= 1;
        }

        //Check for wrap around
        if heading < 0{
            heading = 3;
        }else if heading > 3{
            heading = 0;
        }

        //Move
        for _j in 0..num_move{
            if heading == 0{
                loc[0] = loc[0] + 1;
            }else if heading == 1{
                loc[1] = loc[1] + 1;
            }else if heading == 2{
                loc[0] = loc[0] -  1;
            }else if heading == 3{
                loc[1] = loc[1] - 1;
            }

            if locmem.contains(&loc){
                checker = false;
                break;
            }else{
                locmem.push(loc);
            }
        }

        if !checker{
            break;
        }
    }

    println!("Total distance moved in Part 2: {}", (loc[0].abs() + loc[1].abs()));
}