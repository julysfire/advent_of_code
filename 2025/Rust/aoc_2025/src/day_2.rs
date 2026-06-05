use std::fs;

pub fn day_2_main() {
    part_1();
}

pub fn part_1() {
    //Ingest data
    let file_name = "inputs/day_2.txt";
    let contents = fs::read_to_string(file_name).expect("Failed to read File");

    //Split by each line
    let parts: Vec<&str> = contents.split(",").collect();

    let invalid_sum = 0;

    for i in 0..parts.len() {
        let product_ranges: Vec<&str> = parts[i].split("-").collect();
        let lower_range: usize = product_ranges[0].trim().parse().unwrap();
        let upper_range: usize = product_ranges[1].trim().parse().unwrap();
    }

    println!("The answer to Part 1 is: {}", invalid_sum);
}
