use std::fs;
use regex::Regex; 

pub fn day_1_main() {
    //Ingest data
    let file_name = "inputs/day_1_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

    //Split by each line
    let parts: Vec<&str> = contents.split("\n").collect();

    println!("The answer the Part 1 is: {}", part_1(parts.clone()));
    println!("The answer the Part 2 is: {}", part_2(parts.clone()));
}

fn part_1(parts: Vec<&str>) -> i32 {
    let mut sumr = 0;

    for i in 0..parts.len()-1{
        let mut line: Vec<&str> = parts[i].split("").collect();

        //First Number
        let first_num = get_number(line.clone());

        line.reverse();

        //Second Number
        let second_num = get_number(line.clone());

        let final_num:i32 = (first_num.to_owned() + "" + second_num).parse().unwrap();

        sumr = sumr + final_num;
    }

    return sumr;
}

fn part_2(parts: Vec<&str>) -> i32 {
    let num_spelled = ["one","two","three","four","five","six","seven","eight","nine"];
    let nums = ["1","2","3","4","5","6","7","8","9"];
    let mut sumr = 0;

    for i in 0..parts.len()-1{
        let mut parts_line: String = parts[i].to_string(); 

        
        for j in 0..num_spelled.len(){
            //Need to add first letter of word and last letter of word around the number
            let mut replace_val: String = num_spelled[j].chars().next().unwrap().to_string();
            replace_val = replace_val + nums[j]; 
            replace_val = replace_val + &num_spelled[j].chars().last().unwrap().to_string();

            parts_line = parts_line.replace(num_spelled[j], &replace_val);
        }
        let mut line: Vec<&str> = parts_line.split("").collect();
        //println!("{:?}", line);

        //First Number
        let first_num = get_number(line.clone());

        line.reverse();

        //Second Number
        let second_num = get_number(line.clone());
        let final_num:i32 = (first_num.to_owned() + "" + second_num).parse().unwrap();

        sumr = sumr + final_num;
    }

    return sumr;
}

fn get_number(line: Vec<&str>) -> &str{
    let num_regex = Regex::new(r"[0-9]").unwrap();
    for i in 1..line.len()-1{
        let item_check = line[i];

        if num_regex.is_match(item_check){
            return item_check;
        }
    }

    return "";
}
