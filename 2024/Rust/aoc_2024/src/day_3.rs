use std::fs;
use regex::Regex;

pub fn day_3_main(){
    part_1();
    part_2();
}

fn part_1(){
    //Ingest data
    let file_name = "inputs/day_3_input.txt";
    let contents:String = fs::read_to_string(file_name)
        .expect("Failed to read File");

    let mut breaker:bool = true;
    let mut sumr:i32 = 0;

    while breaker{
        let re = Regex::new(r"mul\(([0-9]|[1-9][0-9]|[1-9][0-9][0-9]),([0-9]|[1-9][0-9]|[1-9][0-9][0-9])\)").unwrap();
        let mut_index:usize = contents.find("mut");

        let n_string:String = contents.chars().skip(mut_index).collect();




        /*
        // TODO: COnvert this down
        mul_index = input_text.find("mul(")
        if mul_index < 0:
            breaker = False
            break

        closing_paren_index = input_text[mul_index:].find(")") + mul_index + 1
        s = input_text[mul_index:closing_paren_index]

        if re.match(r"mul\(([0-9]|[1-9][0-9]|[1-9][0-9][0-9]),([0-9]|[1-9][0-9]|[1-9][0-9][0-9])\)", s):
            x = input_text[mul_index+4:closing_paren_index-1].split(',')
            total_result = total_result + (int(x[0]) * int(x[1]))
        input_text = input_text[mul_index+1:]
        */

        breaker = false;
    }

    println!("Total multiple from Part 1: {}", sumr);
}

fn part_2(){
    //Ingest data
    let file_name = "inputs/day_2_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

    let mut breaker:bool = true;
    let mut sumr:i32 = 0;

    println!("Total multiple from Part 2: {}", sumr);
}
