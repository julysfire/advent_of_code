use std::fs;

pub fn day_6_main(){
    part_1();
    //part_2();
}

fn part_1(){
    //Ingest data
    let file_name = "inputs/day_6_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");
}

fn part_2(){

}
