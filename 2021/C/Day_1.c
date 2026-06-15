#include <stdio.h>
#include <stdlib.h>

void part_1();
void part_2();

int main() {
  part_1();
  part_2();
  return 0;
}

void part_1() {
  FILE *file = fopen("inputs/day_1_input.txt", "r");
  int increased = 0;
  int previous = 0;

  char line[50];

  while (fgets(line, sizeof(line), file) != NULL) {
    if (previous == 0) {
      previous = atoi(line);
    } else {
      int curr = atoi(line);
      if (curr > previous) {
        increased += 1;
      }
      previous = curr;
    }
  }
  fclose(file);

  printf("The answer for Part 1 is: %d\n", increased);
}

void part_2() {
  FILE *file = fopen("inputs/day_1_input.txt", "r");

  int nums[2000] = {};
  int previous = 0;
  int sumr = 0;
  int increased = 0;
  int counter = 0;
  char line[50];

  while (fgets(line, sizeof(line), file) != NULL) {
    nums[counter] = atoi(line);
    counter += 1;
  }
  fclose(file);

  for (int i = 0; i < (sizeof(nums) / sizeof(nums[0])) - 2; i++) {
    sumr = nums[i] + nums[i + 1] + nums[i + 2];
    if (previous != 0) {
      if (sumr > previous) {
        increased += 1;
      }
    }
    previous = sumr;
  }

  printf("The answer for Part 2 is: %d\n", increased);
}
