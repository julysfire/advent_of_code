use std::fs;

pub fn day_4_main(){
    part_1();
    //part_2();
}

//Expecting 984
fn part_1(){
    //Ingest data
    let file_name = "inputs/day_4_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

}

fn _part_2(){

}
