use std::fs;

pub fn day_1_main() {
    //Ingest data
    let file_name = "inputs/day_1_input.txt";
    let contents = fs::read_to_string(file_name).expect("Failed to read File");

    //Split by each line
    let mut parts: Vec<&str> = contents.split("").collect();

    //Get rid of the crap
    parts.remove(0);
    parts.remove(parts.len() - 1);
    parts.remove(parts.len() - 1);

    println!("The answer the Part 1 is: {}", part_1(parts.clone()));
    println!("The answer the Part 2 is: {}", part_2(parts.clone()));
}

fn part_1(parts: Vec<&str>) -> i32 {
    let mut sumr = 0;

    for i in 0..parts.len() {
        let num: i32 = parts[i].parse().unwrap();
        let mut next_num = parts[0].parse().unwrap();

        if i != parts.len() - 1 {
            next_num = parts[i + 1].parse().unwrap();
        }

        if num == next_num {
            sumr += num;
        }
    }

    return sumr;
}

fn part_2(parts: Vec<&str>) -> i32 {
    let mut sumr = 0;
    let halfway: usize = parts.len() / 2;

    for i in 0..parts.len() {
        let num: i32 = parts[i].parse().unwrap();
        let mut next_pos: usize = i + halfway;

        if next_pos >= parts.len() {
            next_pos = next_pos - parts.len();
        }

        let next_num: i32 = parts[next_pos].parse().unwrap();

        if num == next_num {
            sumr += num;
        }
    }

    return sumr;
}
