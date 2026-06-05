use std::fs;

pub fn day_2_main() {
    //Ingest data
    let file_name = "inputs/day_2_input.txt";
    let contents = fs::read_to_string(file_name).expect("Failed to read File");

    //Split by each line
    let parts: Vec<&str> = contents.split("\n").collect();

    println!("The answer the Part 1 is: {}", part_1(parts.clone()));
    println!("The answer the Part 2 is: {}", part_2(parts.clone()));
}

fn part_1(parts: Vec<&str>) -> i32 {
    let mut sumr = 0;

    for i in 0..parts.len() - 1 {
        let nums_str: Vec<&str> = parts[i].split("\t").collect();
        let mut nums: Vec<i32> = Vec::new();

        for j in 0..nums_str.len() {
            if let Ok(_) = nums_str[j].parse::<i32>() {
                nums.push(nums_str[j].parse::<i32>().unwrap());
            }
        }

        nums.sort();

        sumr += nums[nums.len() - 1] - nums[0];
    }

    return sumr;
}

fn part_2(parts: Vec<&str>) -> i32 {
    let mut sumr = 0;

    for i in 0..parts.len() - 1 {
        let nums_str: Vec<&str> = parts[i].split("\t").collect();
        let mut nums: Vec<i32> = Vec::new();

        for j in 0..nums_str.len() {
            if let Ok(_) = nums_str[j].parse::<i32>() {
                nums.push(nums_str[j].parse::<i32>().unwrap());
            }
        }

        'outer: for j in 0..nums.len() {
            for k in 0..nums.len() {
                if j != k && nums[j] % nums[k] == 0 {
                    sumr += nums[j] / nums[k];
                    break 'outer;
                }
            }
        }
    }

    return sumr;
}

