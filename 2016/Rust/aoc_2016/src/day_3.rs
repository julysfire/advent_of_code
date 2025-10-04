use std::fs;

pub fn day_3_main(){
    part_1();
    //part_2();
}

//Expecting 983
fn part_1(){
    //Ingest data
    let file_name = "inputs/day_3_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

    //Split by each line
    let parts: Vec<&str> = contents.split("\n").collect();
    let mut counter: i32 = 0;

    for i in 0..parts.len()-1{
        let mut new_parts: Vec<&str> = parts[i].split("  ").collect();

        //Remove blank string parts
        for _j in 0..4{
            if let Some(pos) = new_parts.iter().position(|x| *x == ""){
                new_parts.remove(pos);
            }
        }

        new_parts[0] = new_parts[0].trim();
        new_parts[1] = new_parts[1].trim();
        new_parts[2] = new_parts[2].trim();


        let tri:[i32; 3] = [new_parts[0].parse().expect("Failed to Parse"),new_parts[1].parse().expect("Failed to Parse"),new_parts[2].parse().expect("Failed to Parse")];


        if tri[0] + tri[1] > tri[2] && tri[1] + tri[2] > tri[0] && tri[2] + tri[0] > tri[1] {
            counter +=1;
        }
    }
    println!("Count of Part 1: {}", counter);
}

fn _part_2(){
    //Ingest data
    let file_name = "inputs/day_3_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");
    
    //Todo
}
