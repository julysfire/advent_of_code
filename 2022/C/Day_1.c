#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void part_1();
void part_2();
void check_arr(int elf, int *arr);

int main() {
  part_1();
  part_2();
}

void part_1() {
  FILE *file = fopen("inputs/day_1_input.txt", "r");
  char line[1000];
  int fattest = 0;
  int cals = 0;

  while (fgets(line, sizeof(line), file) != NULL) {
    int line_cals = atoi(line);

    if (line_cals == 0) {
      if (cals > fattest) {
        fattest = cals;
      }
      cals = 0;
    } else {
      cals += line_cals;
    }
  }
  fclose(file);

  printf("The total cals for the fattest elf is: %d\n", fattest);
}

void part_2() {
  FILE *file = fopen("inputs/day_1_input.txt", "r");
  char line[1000];
  int fattest[3] = {
      1,
      2,
      3,
  };
  int cals = 0;

  while (fgets(line, sizeof(line), file) != NULL) {
    int line_cals = atoi(line);

    if (line_cals == 0) {
      check_arr(cals, fattest);
      cals = 0;
    } else {
      cals += line_cals;
    }
  }
  fclose(file);

  int final_three = fattest[0] + fattest[1] + fattest[2];
  printf("The total cals for the fattest elf is: %d\n", final_three);
}

void check_arr(int elf, int *arr) {
  if (elf > arr[2]) {
    arr[0] = arr[1];
    arr[1] = arr[2];
    arr[2] = elf;
  } else if (elf > arr[1]) {
    arr[0] = arr[1];
    arr[1] = elf;
  } else if (elf > arr[0]) {
    arr[0] = elf;
  }
}
