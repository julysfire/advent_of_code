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

    //Split by each line
    let parts: Vec<&str> = contents.split("\n").collect();
    let mut good_reports: i32 = 0;
    
    for i in 0..parts.len()-1{
        let x: Vec<&str> = parts[i].split(" ").collect();
        let x_i: Vec<i32> = x
            .iter()
            .map(|s| s.parse::<i32>().unwrap())
            .collect();
        let valid = test_validity(x_i);

        if valid{
            good_reports += 1;
        }
    }

    println!("There were {} good reports in Part 1.", good_reports);
}

fn part_2(){
    //Ingest data
    let file_name = "inputs/day_2_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

    //Split by each line
    let parts: Vec<&str> = contents.split("\n").collect();
    let mut good_reports: i32 = 0;
    
    for i in 0..parts.len()-1{
        let x: Vec<&str> = parts[i].split(" ").collect();
        let x_i: Vec<i32> = x
            .iter()
            .map(|s| s.parse::<i32>().unwrap())
            .collect();
        let valid = test_validity(x_i.clone());

        if valid{
            good_reports += 1;
        }else{
            for j in 0..x_i.len(){
                let mut x_z: Vec<i32> = x_i.clone();
                x_z.remove(j);

                let valid = test_validity(x_z.clone());
                if valid{
                    good_reports += 1;
                    break;
                }
            }
        }
    }

    println!("There were {} good reports in Part 2.", good_reports);
}

fn test_validity(arr:Vec<i32>) -> bool {
    let mut direction: &str = if arr[0] > arr[1]{
        "desc"
    }else if arr[1] > arr[0]{
        "asc"
    }else{
        "bad"
    };

    if direction != "bad"{
        for i in 0..arr.len()-1{

            if direction == "asc"{
                if (arr[i + 1] >= (arr[i] + 1)) && (arr[i + 1] <= (arr[i] + 3)){
                }
                else{
                    direction = "bad"
                }
            } else {
                if (arr[i + 1] <= (arr[i] - 1)) && (arr[i + 1] >= (arr[i] - 3)){
                }
                else{
                    direction = "bad"
                }
            }
        }
    }

    if direction != "bad"{
        return true 
    }else{
        return false
    }
}
