#include <fstream>
#include <iostream>
#include <vector>

void part_1();
void part_2();
std::vector<std::string> parse_input();

void part_1() {
  std::vector<std::string> day_data = parse_input();
  int sumr = 0;
  std::string alpha_lower = "abcdefghijklmnopqrstuvwxyz";
  std::string alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

  for (size_t i = 0; i < day_data.size(); i++) {
    std::string x = day_data[i];
    int x_size = x.length() / 2;
    std::string s1 = x.substr(0, x_size);
    std::string s2 = x.substr(x_size, x_size);

    char item_match;
    for (size_t j = 0; j < s1.length(); j++) {
      char find_s = s1[j];
      int find_loc = s2.find(find_s);

      if (find_loc > -1) {
        item_match = find_s;
        break;
      }
    }

    int find_l = alpha_lower.find(item_match);
    if (find_l < 0) {
      find_l = alpha_upper.find(item_match) + 27;
    } else {
      find_l += 1;
    }

    sumr += find_l;
  }

  std::cout << "The answer to Part 1 is : " << sumr << std::endl;
}
void part_2() {
  std::vector<std::string> day_data = parse_input();
  int sumr = 0;
  std::string alpha_lower = "abcdefghijklmnopqrstuvwxyz";
  std::string alpha_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

  for (size_t i = 0; i < day_data.size(); i += 3) {
    std::string s1 = day_data[i];
    std::string s2 = day_data[i + 1];
    std::string s3 = day_data[i + 2];
    std::string longest;
    char item_match;

    if (s1.length() > s2.length() && s1.length() > s3.length()) {
      longest = s1;
    } else if (s2.length() > s1.length() && s2.length() > s3.length()) {
      longest = s2;
    } else {
      longest = s3;
    }

    for (size_t j = 0; j < longest.length(); j++) {
      char checker = longest[j];
      int find_1 = s1.find(checker);
      int find_2 = s2.find(checker);
      int find_3 = s3.find(checker);

      if (find_1 > -1 && find_2 > -1 && find_3 > -1) {
        item_match = checker;
        break;
      }
    }

    int find_l = alpha_lower.find(item_match);
    if (find_l < 0) {
      find_l = alpha_upper.find(item_match) + 27;
    } else {
      find_l += 1;
    }

    sumr += find_l;
  }

  std::cout << "The answer to Part 2 is : " << sumr << std::endl;
}

int main() {
  part_1();
  part_2();
  return 0;
}

std::vector<std::string> parse_input() {
  std::vector<std::string> nums;
  std::ifstream f("Inputs/day_3_input.txt");

  std::string s;

  while (getline(f, s)) {
    nums.push_back(s);
  }

  f.close();

  return nums;
}
