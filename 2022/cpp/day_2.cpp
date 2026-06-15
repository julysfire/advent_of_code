#include <cmath>
#include <fstream>
#include <iostream>
#include <vector>

void part_1();
void part_2();
std::vector<std::string> parse_input();

int main() {
  part_1();
  part_2();
  return 0;
}

void part_1() {
  std::vector<std::string> data_in = parse_input();
  int round_score = 0;
  int total_score = 0;

  for (size_t i = 0; i < data_in.size(); i++) {
    std::string elf_pick = data_in[i].substr(0, 1);
    std::string you_pick = data_in[i].substr(2, 1);

    if (you_pick == "X") {
      round_score += 1;
    } else if (you_pick == "Y") {
      round_score += 2;
    } else {
      round_score += 3;
    }

    if (elf_pick == "A") {
      if (you_pick == "X") {
        round_score += 3;
      } else if (you_pick == "Y") {
        round_score += 6;
      }
    } else if (elf_pick == "B") {
      if (you_pick == "Y") {
        round_score += 3;
      } else if (you_pick == "Z") {
        round_score += 6;
      }
    } else {
      if (you_pick == "Z") {
        round_score += 3;
      } else if (you_pick == "X") {
        round_score += 6;
      }
    }

    total_score += round_score;
    round_score = 0;
  }

  std::cout << "The total score for Part 1: " << total_score << std::endl;
}

void part_2() {
  std::vector<std::string> data_in = parse_input();
  int round_score = 0;
  int total_score = 0;
  for (size_t i = 0; i < data_in.size(); i++) {
    std::string elf_pick = data_in[i].substr(0, 1);
    std::string you_pick = data_in[i].substr(2, 1);

    if (you_pick == "X") {
      if (elf_pick == "A") {
        round_score += 3;
      } else if (elf_pick == "B") {
        round_score += 1;
      } else {
        round_score += 2;
      }
    } else if (you_pick == "Y") {
      if (elf_pick == "A") {
        round_score += 4;
      } else if (elf_pick == "B") {
        round_score += 5;
      } else {
        round_score += 6;
      }
    } else {
      if (elf_pick == "A") {
        round_score += 8;
      } else if (elf_pick == "B") {
        round_score += 9;
      } else {
        round_score += 7;
      }
    }

    total_score += round_score;
    round_score = 0;
  }

  std::cout << "The total score for Part 2: " << total_score << std::endl;
}

std::vector<std::string> parse_input() {
  std::vector<std::string> nums;
  std::ifstream f("Inputs/day_2_input.txt");

  std::string s;

  while (getline(f, s)) {
    nums.push_back(s);
  }

  f.close();

  return nums;
}
