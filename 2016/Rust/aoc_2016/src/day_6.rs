use std::fs;

pub fn day_6_main(){
    part_1();
    part_2();
}

fn part_1(){
    //Ingest data
    let file_name = "inputs/day_6_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");
    let parts: Vec<&str> = contents.split("\n").collect();

    
    let mut v1: String = String::new();
    let mut v2: String = String::new();
    let mut v3: String = String::new();
    let mut v4: String = String::new();
    let mut v5: String = String::new();
    let mut v6: String = String::new();
    let mut v7: String = String::new();
    let mut v8: String = String::new();

    for i in 0..parts.len()-1{
        let indv: Vec<&str> = parts[i].split("").collect();

        v1 = v1 + indv[1];
        v2 = v2 + indv[2];
        v3 = v3 + indv[3];
        v4 = v4 + indv[4];
        v5 = v5 + indv[5];
        v6 = v6 + indv[6];
        v7 = v7 + indv[7];
        v8 = v8 + indv[8];
    }

    let sorted_counted_vec_1:Vec<(char,usize)> = sort_vec(v1,false);
    let sorted_counted_vec_2:Vec<(char,usize)> = sort_vec(v2,false);
    let sorted_counted_vec_3:Vec<(char,usize)> = sort_vec(v3,false);
    let sorted_counted_vec_4:Vec<(char,usize)> = sort_vec(v4,false);
    let sorted_counted_vec_5:Vec<(char,usize)> = sort_vec(v5,false);
    let sorted_counted_vec_6:Vec<(char,usize)> = sort_vec(v6,false);
    let sorted_counted_vec_7:Vec<(char,usize)> = sort_vec(v7,false);
    let sorted_counted_vec_8:Vec<(char,usize)> = sort_vec(v8,false);

    let mut final_string:String = String::new();
    final_string.push(sorted_counted_vec_1[0].0);
    final_string.push(sorted_counted_vec_2[0].0);
    final_string.push(sorted_counted_vec_3[0].0);
    final_string.push(sorted_counted_vec_4[0].0);
    final_string.push(sorted_counted_vec_5[0].0);
    final_string.push(sorted_counted_vec_6[0].0);
    final_string.push(sorted_counted_vec_7[0].0);
    final_string.push(sorted_counted_vec_8[0].0);

    println!("The secret message in part 1 is : {}", final_string);
}

fn sort_vec(n_string:String, rev_flag:bool) -> Vec<(char, usize)>{
    let mut sorted: Vec<(char, usize)> = Vec::new();
    let alpha: Vec<char> = "abcdefghijklmnopqrstuvwxyz".chars().collect();

    //Count each letter in array
    for j in 0..alpha.len(){
        let char_count = n_string.chars().filter(|c| *c == alpha[j]).count();
          sorted.push((alpha[j], char_count));
    }
    if rev_flag{
        sorted.sort_by(|a, b| a.1.cmp(&b.1));

    }else{
        sorted.sort_by(|a, b| b.1.cmp(&a.1));
    }

    return sorted;
}

fn part_2(){
    //Ingest data
    let file_name = "inputs/day_6_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");
    let parts: Vec<&str> = contents.split("\n").collect();

    
    let mut v1: String = String::new();
    let mut v2: String = String::new();
    let mut v3: String = String::new();
    let mut v4: String = String::new();
    let mut v5: String = String::new();
    let mut v6: String = String::new();
    let mut v7: String = String::new();
    let mut v8: String = String::new();

    for i in 0..parts.len()-1{
        let indv: Vec<&str> = parts[i].split("").collect();

        v1 = v1 + indv[1];
        v2 = v2 + indv[2];
        v3 = v3 + indv[3];
        v4 = v4 + indv[4];
        v5 = v5 + indv[5];
        v6 = v6 + indv[6];
        v7 = v7 + indv[7];
        v8 = v8 + indv[8];
    }

    let sorted_counted_vec_1:Vec<(char,usize)> = sort_vec(v1,true);
    let sorted_counted_vec_2:Vec<(char,usize)> = sort_vec(v2,true);
    let sorted_counted_vec_3:Vec<(char,usize)> = sort_vec(v3,true);
    let sorted_counted_vec_4:Vec<(char,usize)> = sort_vec(v4,true);
    let sorted_counted_vec_5:Vec<(char,usize)> = sort_vec(v5,true);
    let sorted_counted_vec_6:Vec<(char,usize)> = sort_vec(v6,true);
    let sorted_counted_vec_7:Vec<(char,usize)> = sort_vec(v7,true);
    let sorted_counted_vec_8:Vec<(char,usize)> = sort_vec(v8,true);

    let mut final_string:String = String::new();
    final_string.push(sorted_counted_vec_1[0].0);
    final_string.push(sorted_counted_vec_2[0].0);
    final_string.push(sorted_counted_vec_3[0].0);
    final_string.push(sorted_counted_vec_4[0].0);
    final_string.push(sorted_counted_vec_5[0].0);
    final_string.push(sorted_counted_vec_6[0].0);
    final_string.push(sorted_counted_vec_7[0].0);
    final_string.push(sorted_counted_vec_8[0].0);

    println!("The secret message in part 2 is : {}", final_string);
}
