use std::fs;
use regex::Regex;

pub fn day_5_main(){
    //part_1();
    part_2();
}

fn part_1(){
    //Ingest data
    let file_name = "inputs/day_5_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

    let mut num = 0;
    let mut sixth_char:String = String::new();

    loop{
        let test_string: &str = &(contents.clone() + &num.to_string()).replace("\n","");

        let digest_str = hash_value(test_string);
        let first_five = &digest_str[..5];
        if first_five == "00000"{
            let push:String = digest_str.chars().skip(5).take(1).collect();
            sixth_char.push_str(&push);
            println!("{}", sixth_char.len());
        }
        if sixth_char.len() == 8{
            break;
        }
        num += 1;

    }

    println!("The password for Part 1 is: {}", sixth_char);
}

fn part_2(){
    //Ingest data
    let file_name = "inputs/day_5_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

    let mut num = 0;
    let mut password:[String; 8] = ["".to_string(),"".to_string(),"".to_string(),"".to_string(),"".to_string(),"".to_string(),"".to_string(),"".to_string()];
    let mut counter: i32 = 0;
    let re = Regex::new(r"[0-7]").unwrap();

    loop{
        let test_string: &str = &(contents.clone() + &num.to_string()).replace("\n","");

        let digest_str = hash_value(test_string);
        let first_five = &digest_str[..5];
        if first_five == "00000"{

            let pos:String = digest_str.chars().skip(5).take(1).collect();
            
            if re.is_match(&pos){
                let pos_parsed:i32 = pos.parse().expect("Couldn't parse position");
                let char_to_put:String = digest_str.chars().skip(6).take(1).collect();

                if password[pos_parsed as usize] == ""{
                    password[pos_parsed as usize] = char_to_put;
                    counter += 1;
                }
            }
        }
        if counter == 8{
            break;
        }
        num += 1;
    }

    println!("The password for Part 2 is: {}", password.join(""));
}

fn hash_value(hash_string: &str) -> String{
    let digest = md5::compute(hash_string);
    let hashed_str = format!("{:x}", digest);

    return hashed_str;
}
