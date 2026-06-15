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
  std::vector<std::string> instructs = parse_input();
  int horizontal = 0;
  int vertical = 0;

  for (int i = 0; i < instructs.size(); i++) {
    std::string line_i = instructs[i];
    int spacer = line_i.find(" ");

    std::string dir = line_i.substr(0, spacer);
    int num = stoi(line_i.substr(spacer + 1, (line_i.length() - spacer - 1)));

    if (dir == "up") {
      vertical -= num;
    } else if (dir == "down") {
      vertical += num;
    } else if (dir == "forward") {
      horizontal += num;
    }
  }

  int final_s = horizontal * vertical;
  std::cout << "The final answer for Part 1 is: " << final_s << std::endl;
}

void part_2() {
  std::vector<std::string> instructs = parse_input();
  int horizontal = 0;
  int vertical = 0;
  int aim = 0;

  for (int i = 0; i < instructs.size(); i++) {
    std::string line_i = instructs[i];
    int spacer = line_i.find(" ");

    std::string dir = line_i.substr(0, spacer);
    int num = stoi(line_i.substr(spacer + 1, (line_i.length() - spacer - 1)));

    if (dir == "up") {
      aim -= num;
    } else if (dir == "down") {
      aim += num;
    } else if (dir == "forward") {
      horizontal += num;
      vertical += (aim * num);
    }
  }

  int final_s = horizontal * vertical;
  std::cout << "The final answer for Part 1 is: " << final_s << std::endl;
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
