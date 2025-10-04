use std::fs;
use std::sync::{Arc};
use std::sync::atomic::{AtomicU64, Ordering};
use std::thread;

pub fn day_4_main(){
    part_1();
    part_2();
}

fn part_1(){
    //Ingest data
    let file_name = "inputs/day_4_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");

    let mut num = 0;

    loop{
        let test_string: &str = &(contents.clone() + &num.to_string()).replace("\n","");

        let digest_str = hash_value(test_string);
        let first_five = &digest_str[..5];
        if first_five == "00000"{
            break;
        }

        num += 1;
    }

    println!("The first number in Part 1 is: {}", num);
}

fn part_2(){
    //Ingest data
    let file_name = "inputs/day_4_input.txt";
    let contents = fs::read_to_string(file_name)
        .expect("Failed to read File");
    let base = Arc::new(contents);

    let counter = Arc::new(AtomicU64::new(0));
    let found = Arc::new(AtomicU64::new(u64::MAX));

    let threads = match std::thread::available_parallelism() {
        Ok(n) => n.get(),
        Err(_) => 4,
    };

    let mut handles = Vec::new();
    for _ in 0..threads {
        let base = Arc::clone(&base);
        let counter = Arc::clone(&counter);
        let found = Arc::clone(&found);

        let handle = thread::spawn(move || {
            loop {
                // Get next candidate
                let i = counter.fetch_add(1, Ordering::Relaxed);

                // If we've already found a smaller or equal solution, stop.
                let best = found.load(Ordering::Acquire);
                if i >= best {
                    break;
                }

                let test_string = format!("{}{}", base.as_str(), i);
                let digest_str = hash_value(&test_string);

                if &digest_str[..6] == "000000" {
                    // Attempt to set a new best (smallest) value.
                    let mut cur = found.load(Ordering::Relaxed);
                    while i < cur {
                        match found.compare_exchange(cur, i, Ordering::AcqRel, Ordering::Acquire) {
                            Ok(_) => break,
                            Err(prev) => cur = prev,
                        }
                    }
                    // Once updated (or if someone else wrote a smaller), other
                    // threads will see it and stop when appropriate.
                }
            }
        });

        handles.push(handle);
    }

    for h in handles {
        let _ = h.join();
    }

    let result = found.load(Ordering::Relaxed);
    if result == u64::MAX {
        println!("No number found for Part 2");
    } else {
        println!("The first number in Part 2 is: {}", result);
    }
}

fn hash_value(hash_string: &str) -> String{
    let digest = md5::compute(hash_string);
    let hashed_str = format!("{:x}", digest);

    return hashed_str;
}
