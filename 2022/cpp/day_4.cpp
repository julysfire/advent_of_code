#include "headers/stringandvectorutils.h"
#include <fstream>
#include <iostream>
#include <vector>

void part_1();
void part_2();
std::vector<std::string> parse_input();

void part_1() {
  std::vector<std::string> day_data = parse_input();
  int sumr = 0;

  for (size_t i = 0; i < day_data.size(); i++) {
    std::string item = day_data[i];
    std::vector<std::string> vec_list = split_string_to_list(item, ',');

    std::vector<std::string> shift_1_s = split_string_to_list(vec_list[0], '-');
    std::vector<std::string> shift_2_s = split_string_to_list(vec_list[1], '-');

    std::vector<int> shift_1 = vector_string_to_int(shift_1_s);
    std::vector<int> shift_2 = vector_string_to_int(shift_2_s);

    if ((shift_1[0] <= shift_2[0] && shift_1[1] >= shift_2[1]) ||
        (shift_2[0] <= shift_1[0] && shift_2[1] >= shift_1[1])) {
      sumr += 1;
    }
  }

  std::cout << "The answer to part 1 is: " << sumr << std::endl;
}

void part_2() {
  std::vector<std::string> day_data = parse_input();
  int sumr = 0;

  for (size_t i = 0; i < day_data.size(); i++) {
    std::string item = day_data[i];
    std::vector<std::string> vec_list = split_string_to_list(item, ',');

    std::vector<std::string> shift_1_s = split_string_to_list(vec_list[0], '-');
    std::vector<std::string> shift_2_s = split_string_to_list(vec_list[1], '-');

    std::vector<int> shift_1 = vector_string_to_int(shift_1_s);
    std::vector<int> shift_2 = vector_string_to_int(shift_2_s);

    if ((shift_1[0] <= shift_2[0] && shift_1[1] >= shift_2[1]) ||
        (shift_2[0] <= shift_1[0] && shift_2[1] >= shift_1[1])) {
      sumr += 1;
    } else if (shift_1[1] >= shift_2[0] && shift_1[1] <= shift_2[1]) {
      sumr += 1;
    } else if (shift_1[0] >= shift_2[0] && shift_1[0] <= shift_2[1]) {
      sumr += 1;
    }
  }

  std::cout << "The answer to part 2 is: " << sumr << std::endl;
}

int main() {
  part_1();
  part_2();
  return 0;
}

std::vector<std::string> parse_input() {
  std::vector<std::string> nums;
  std::ifstream f("Inputs/day_4_input.txt");

  std::string s;

  while (getline(f, s)) {
    nums.push_back(s);
  }

  f.close();

  return nums;
}
