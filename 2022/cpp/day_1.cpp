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
  std::vector<std::string> nums = parse_input();
  int cals = 0;
  int fattest = 0;

  for (size_t i = 0; i < nums.size(); i++) {
    std::string ele = nums[i];
    if (ele == "") {
      if (cals > fattest) {
        fattest = cals;
      }
      cals = 0;
    } else {
      cals += stoi(ele);
    }
  }

  std::cout << "The total calories for Part 1: " << fattest << std::endl;
}

void part_2() {
  std::vector<std::string> nums = parse_input();
  std::vector<int> elfs_totals;
  int cals = 0;

  for (size_t i = 0; i < nums.size(); i++) {
    std::string ele = nums[i];
    if (ele == "") {
      elfs_totals.push_back(cals);
      cals = 0;
    } else {
      cals += stoi(ele);
    }
  }

  std::sort(elfs_totals.begin(), elfs_totals.end(), std::greater<int>());
  int fattest_three = elfs_totals[0] + elfs_totals[1] + elfs_totals[2];

  std::cout << "The total calories for Part 2: " << fattest_three << std::endl;
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
