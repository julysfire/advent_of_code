#include "stringandvectorutils.h"
#include <string>

std::vector<std::string> split_string_to_list(std::string s, char delim) {
  std::vector<std::string> n_vec;
  int x = s.find(delim);

  while (x > -1) {
    std::string y = s.substr(0, x);
    n_vec.push_back(y);
    s = s.substr(x + 1, s.length() - x);

    x = s.find(delim);
    if (x == -1) {
      n_vec.push_back(s);
    }
  }

  return n_vec;
}

std::vector<int> vector_string_to_int(const std::vector<std::string> s) {
  std::vector<int> n_vec;

  for (size_t i = 0; i < s.size(); i++) {
    n_vec.push_back(std::stoi(s[i]));
  }

  return n_vec;
};
