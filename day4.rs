use std::collections::HashSet;
use std::fs;


fn main() {
    let test_input = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
";

    let mut total: u32 = 0;
    for line in test_input.lines() {
        total += tally_points(line);
    }
    println!("Test Points: {}", total);   

    total = 0;
    let data = fs::read_to_string("input-day4.txt").expect("Can't open data file");
    for line in data.lines() {
        total += tally_points(line);
    }
    println!("Part 1 Points: {}", total);   
    
}

fn tally_points(line: &str) -> u32 {
    let fields: Vec<&str> = line.split([':', '|']).collect();
    let have: HashSet<&str> = HashSet::from_iter(fields[1].trim().split_whitespace());
    let win: HashSet<&str> = HashSet::from_iter(fields[2].trim().split_whitespace());
    let matches = have.intersection(&win).count() as u32;
    if matches > 0 {
        2u32.pow(matches - 1)
    } else {
        0
    }
}
