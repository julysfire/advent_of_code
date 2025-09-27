use std::fs;

pub fn day_1_main() {
    //Ingest data
    let file_name = "inputs/day_1_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

    //Split by each line
    let parts: Vec<&str> = contents.split("\n").collect();

    //Vectors for holding data
    let mut vec1: Vec<i32> = Vec::new();
    let mut vec2: Vec<i32> = Vec::new();

    //Loop through vectors, take each value, convert to i32 and push to vec1/vecw
    for i in 0..parts.len()-1{
        let sp: Vec<&str> = parts[i].split("   ").collect();
        for j in (0..sp.len()).step_by(2){
            vec1.push(sp[j].parse().expect("Not a number"));
            vec2.push(sp[j+1].parse().expect("Not a number"));
        }
    }
    
    //Clone them before they change, probably a better way of going about this
    let vec1_2: Vec<i32> = vec1.clone();
    let vec2_2: Vec<i32> = vec2.clone();

    let part_1_distance = part_1(vec1, vec2);
    println!("Total Distance for Part 1: {}", part_1_distance);

    let part_2_similar_score = part_2(vec1_2, vec2_2);
    println!("Similarity Score for Part 2: {}", part_2_similar_score);
}

fn part_1(mut list_1: Vec<i32>, mut list_2: Vec<i32>) -> i32 {
    list_1.sort();
    list_2.sort();
    
    let mut total_distance: i32 = 0;

    for i in 0..list_1.len(){
        total_distance = total_distance + (list_1[i] - list_2[i]).abs();
    }
    
    return total_distance;
}

fn part_2(list_1: Vec<i32>, list_2: Vec<i32>) -> i32 {
    let mut similar_score: i32 = 0;

    for i in 0..list_1.len(){
        let mut count_from_list: i32 = 0;
        for j in 0..list_2.len(){
            if list_1[i] == list_2[j]{
                count_from_list += 1;
            }
        }
        similar_score = similar_score + (count_from_list * list_1[i]);
    }
    return similar_score;
}
