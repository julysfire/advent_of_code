#include <algorithm>
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
  std::vector<std::string> lines = parse_input();
  std::vector<std::string> d_1;
  std::vector<std::string> d_2;
  int total_distance = 0;

  for (int i = 0; i < lines.size(); i++) {
    d_1.push_back(lines[i].substr(0, 5));
    d_2.push_back(lines[i].substr(8, 5));
  }

  sort(d_1.begin(), d_1.end());
  sort(d_2.begin(), d_2.end());

  for (int i = 0; i < d_1.size(); i++) {
    total_distance = total_distance + abs(stoi(d_1[i]) - stoi(d_2[i]));
  }

  std::cout << "The total distance for Part 1 is: " << total_distance
            << std::endl;
}

void part_2() {
  std::vector<std::string> lines = parse_input();
  int similar_score = 0;
  std::vector<std::string> d_1;
  std::vector<std::string> d_2;

  for (int i = 0; i < lines.size(); i++) {
    d_1.push_back(lines[i].substr(0, 5));
    d_2.push_back(lines[i].substr(8, 5));
  }

  for (int i = 0; i < d_1.size(); i++) {
    int count_from_list = 0;
    for (int j = 0; j < d_2.size(); j++) {
      if (d_1[i] == d_2[j]) {
        count_from_list += 1;
      }
    }
    similar_score = similar_score + (count_from_list * stoi(d_1[i]));
  }

  std::cout << "The total similar score for Part 2 is: " << similar_score
            << std::endl;
}

std::vector<std::string> parse_input() {
  std::vector<std::string> nums;
  std::ifstream f("Inputs/day_1_input.txt");

  std::string s;

  while (getline(f, s)) {
    nums.push_back(s);
  }

  f.close();

  return nums;
}
