use std::fs;
use regex::Regex; 

pub fn day_2_main() {
    //Ingest data
    let file_name = "inputs/day_2_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

    //Split by each line
    let parts: Vec<&str> = contents.split("\n").collect();

    println!("The answer the Part 1 is: {}", part_1(parts.clone()));
}

fn part_1(parts: Vec<&str>) -> i32 {
    let mut sumr = 0;
    return sumr;
}
