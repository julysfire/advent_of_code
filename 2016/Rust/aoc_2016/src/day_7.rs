
use std::fs;

pub fn day_7_main(){
    part_1();
    part_2();
}

fn part_1(){
    //Ingest data
    let file_name = "inputs/day_7_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");
    let parts: Vec<&str> = contents.split("\n").collect();

    let mut counter:usize = 0;

    for i in 0..parts.len()-1{
        let letters: Vec<char> = parts[i].chars().collect();

        let mut bracket: usize = 0;
        let mut valid: bool = false;

        for j in 0..letters.len()-3{
            if letters[j] == '['{
                bracket += 1;
            }else if letters[j] == ']'{
                bracket -= 1;
            }

            let mut abba_test:Vec<char>= Vec::new();
            abba_test.push(letters[j]);
            abba_test.push(letters[j+1]);
            abba_test.push(letters[j+2]);
            abba_test.push(letters[j+3]);

            if abba_checker(abba_test.clone()){
                println!("Test VEC: {:?},  Whole line:{:?}", abba_test, letters);
                if bracket == 0{
                    valid = true;    
                }else{
                    println!("{:?} is bad!", abba_test);
                    valid = false;
                    break;
                }
            }
        }
        if valid {
            counter += 1;
        }
    }

    println!("The amount of valid IPs in Part 1 is: {}", counter);
}

fn abba_checker(test_vec:Vec<char>) -> bool{
    if test_vec[0] == test_vec[3] && test_vec[1] == test_vec[2] && test_vec[0] != '[' && test_vec[0] != ']' && test_vec[1] != '[' && test_vec[1] != ']' {
        //Should be different
        if test_vec[0] == test_vec[3] && test_vec[0] == test_vec[2] && test_vec[0] == test_vec[1]{
            return false;
        }else{
            return true;
        }
    }else{
        return false;
    }
}

fn part_2(){
    //Ingest data
    let file_name = "inputs/day_7_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");
    let parts: Vec<&str> = contents.split("\n").collect();

    let mut counter:usize = 0;

    for i in 0..parts.len()-1{
        let letters: Vec<char> = parts[i].chars().collect();

    }
}
