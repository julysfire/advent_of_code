
use std::fs;

pub fn day_8_main(){
    part_1();
    //part_2();
}

fn part_1(){
    //Ingest data
    let file_name = "inputs/day_7_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");
    let parts: Vec<&str> = contents.split("\n").collect();

}

fn //part_2(){
    //Ingest data
    let file_name = "inputs/day_7_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");
    let parts: Vec<&str> = contents.split("\n").collect();

}
