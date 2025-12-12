use std::fs;

pub fn day_4_main(){
    part_1();
    part_2();
}

fn part_1(){
    //Ingest data
    let file_name = "inputs/day_4_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

    let mut sumr: i32 = 0;
    let alpha: Vec<char> = "abcdefghijklmnopqrstuvwxyz".chars().collect();

    let parts: Vec<&str> = contents.split("\n").collect();
    //For each line in the txt file
    for i in 0..parts.len()-1{
        //Split apart the room and checksum
        let line: Vec<&str> = parts[i].split("[").collect();

        let main_string:&str = line[0];
        let x:String = line[1].replace("]", "");
        let checksum: Vec<&str> = x.split("").collect();

        let mut sorted: Vec<(char, usize)> = Vec::new();

        //Count each letter in array
        for j in 0..alpha.len(){
            let char_count = main_string.chars().filter(|c| *c == alpha[j]).count();
              sorted.push((alpha[j], char_count));
        }
        sorted.sort_by(|a, b| b.1.cmp(&a.1));

        let mut valid_checksum: bool = true;

        //Check if each letter in the checksum is correct and valid
        for j in 1..checksum.len()-1{
            let checksum_char: Vec<char> = checksum[j].chars().collect();

            if checksum_char[0] != sorted[j-1].0{
                valid_checksum = false;
            }
        }

        //If it is a valid, get the room id and add to sumr
        if valid_checksum{
            let room_id:String = main_string.chars().skip(main_string.len()-3).take(3).collect();
            let room_id_int:i32 = room_id.parse().expect("Couldn't parse room ID.");

            sumr += room_id_int;

        }
    }

    println!("This sum of the sector IDs for real rooms in Part 1 are: {}", sumr);
}


fn part_2(){
    //Ingest data
    let file_name = "inputs/day_4_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

    let alpha: Vec<char> = "abcdefghijklmnopqrstuvwxyz".chars().collect();

    let parts: Vec<&str> = contents.split("\n").collect();
    //For each line in the txt file
    for i in 0..parts.len()-1{
        //Split apart the room and checksum
        let line: Vec<&str> = parts[i].split("[").collect();

        let main_string:&str = line[0];
        let x:String = line[1].replace("]", "");
        let checksum: Vec<&str> = x.split("").collect();

        let mut sorted: Vec<(char, usize)> = Vec::new();

        //Count each letter in array
        for j in 0..alpha.len(){
            let char_count = main_string.chars().filter(|c| *c == alpha[j]).count();
              sorted.push((alpha[j], char_count));
        }
        sorted.sort_by(|a, b| b.1.cmp(&a.1));

        let mut valid_checksum: bool = true;

        //Check if each letter in the checksum is correct and valid
        for j in 1..checksum.len()-1{
            let checksum_char: Vec<char> = checksum[j].chars().collect();

            if checksum_char[0] != sorted[j-1].0{
                valid_checksum = false;
            }
        }

        //If it is a valid, get the room id and add to sumr
        if valid_checksum{
            let room_id:String = main_string.chars().skip(main_string.len()-3).take(3).collect();
            let mut room_id_int:usize = room_id.parse().expect("Couldn't parse room ID.");
            room_id_int = room_id_int % 26;

            let mut char_vec:Vec<char> = main_string.chars().take(main_string.len()-4).collect();

            for z in 0..char_vec.len(){
                if let Some(index) = alpha.iter().position(|&zy| zy == char_vec[z]){
                    let mut new_index = index + room_id_int;

                    if new_index > 25{
                        new_index -= 26;
                    }

                    char_vec[z] = alpha[new_index];
                }
            }

            let mut decrypted_name:String = char_vec.into_iter().collect();
            decrypted_name = decrypted_name.replace("-", " ");

            println!("{:?}, RoomID: {}", decrypted_name, room_id);

            //GREP The output
        }
    }
}
