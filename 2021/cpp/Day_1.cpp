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
  std::vector<std::string> depths = parse_input();
  int increased = 0;

  for (int i = 1; i < depths.size(); i++) {
    if (stoi(depths[i]) > stoi(depths[i - 1])) {
      increased++;
    }
  }

  std::cout << "The total incrased depths for Part 1 is: " << increased
            << std::endl;
}
void part_2() {
  std::vector<std::string> depths = parse_input();
  int increased = 0;
  int previous = 0;

  for (int i = 0; i < depths.size() - 2; i++) {
    int current = stoi(depths[i]) + stoi(depths[i + 1]) + stoi(depths[i + 2]);

    if (previous != 0) {
      if (current > previous) {
        increased++;
      }
    }
    previous = current;
  }

  std::cout << "The total incrased depths for Part 1 is: " << increased
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
