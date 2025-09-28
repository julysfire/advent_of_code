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

    let parts: Vec<&str> = contents.split("\n").collect();
    let mut total_dims:i32 = 0;

    for i in 0..parts.len()-1{
        let prezzies: Vec<&str> = parts[i].split("x").collect();
        let x: i32 = prezzies[0].parse()
            .expect("Couldn't convert to i32.");
        let y: i32 = prezzies[1].parse()
            .expect("Couldn't convert to i32.");
        let z: i32 = prezzies[2].parse()
            .expect("Couldn't convert to i32.");
        
        //2(lw + wh + hl)
        let prezzie_dimen:i32 = (2 * (x*y)) + (2* (y*z)) + (2* (z*x));
        
        //Slack 
        let slack:i32 = 
            if x*y <= y*z && x*y <= z*x { x*y }
            else if y*z <= x*y && y*z <= z*x { y*z }
            else { z*x };

        total_dims = total_dims + prezzie_dimen + slack;
    }

    println!("Total prezzie dimensions in Part 1: {}", total_dims);
}

fn part_2(){
    //Ingest data
    let file_name = "inputs/day_2_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

    let parts: Vec<&str> = contents.split("\n").collect();
    let mut total_dims: i32 = 0;

    for i in 0..parts.len()-1{
        let prezzies: Vec<&str> = parts[i].split("x").collect();
        let x: i32 = prezzies[0].parse()
            .expect("Couldn't convert to i32.");
        let y: i32 = prezzies[1].parse()
            .expect("Couldn't convert to i32.");
        let z: i32 = prezzies[2].parse()
            .expect("Couldn't convert to i32.");

        let bow = x*y*z;

        let mut prez: [i32; 3] = [x,y,z];
        prez.sort();
        let ribbon = prez[0] + prez[0] + prez[1] + prez[1];

        total_dims = total_dims + ribbon + bow;
    }

    println!("Total prezzie dimensions in Part 1: {}", total_dims);
}
