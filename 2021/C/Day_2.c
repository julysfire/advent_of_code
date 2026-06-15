#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void part_1();
void part_2();

int main() {
  part_1();
  part_2();
  return 0;
}

void part_1() {
  FILE *file = fopen("inputs/day_2_input.txt", "r");
  int vertical = 0;
  int horizontal = 0;

  char line[50];

  while (fgets(line, sizeof(line), file) != NULL) {
    char *token;

    token = strtok(line, " ");
    char instruct[8];
    strcpy(instruct, token);

    token = strtok(NULL, " ");
    int num = atoi(token);

    if (strcmp(instruct, "up") == 0) {
      vertical -= num;
    } else if (strcmp(instruct, "down") == 0) {
      vertical += num;
    } else if (strcmp(instruct, "forward") == 0) {
      horizontal += num;
    }
  }
  fclose(file);

  printf("The final result for Part 1 is: %d\n", vertical * horizontal);
}

void part_2() {
  FILE *file = fopen("inputs/day_2_input.txt", "r");
  int vertical = 0;
  int horizontal = 0;
  int aim = 0;

  char line[50];

  while (fgets(line, sizeof(line), file) != NULL) {
    char *token;

    token = strtok(line, " ");
    char instruct[8];
    strcpy(instruct, token);

    token = strtok(NULL, " ");
    int num = atoi(token);

    if (strcmp(instruct, "up") == 0) {
      aim -= num;
    } else if (strcmp(instruct, "down") == 0) {
      aim += num;
    } else if (strcmp(instruct, "forward") == 0) {
      horizontal += num;
      vertical += (aim * num);
    }
  }

  fclose(file);

  printf("The final result for Part 1 is: %d\n", vertical * horizontal);
}
