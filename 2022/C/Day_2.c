#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void part_1();
void part_2();

int main() {
  part_1();
  part_2();
}

void part_1() {
  FILE *file = fopen("inputs/day_2_input.txt", "r");
  char line[1000];
  int total_score = 0;

  while (fgets(line, sizeof(line), file) != NULL) {
    int round_score = 0;
    char elf_pick = line[0];
    char you_pick = line[2];

    if (you_pick == 'X') {
      round_score += 1;
    } else if (you_pick == 'Y') {
      round_score += 2;
    } else {
      round_score += 3;
    }

    if (elf_pick == 'A') {
      if (you_pick == 'X') {
        round_score += 3;
      } else if (you_pick == 'Y') {
        round_score += 6;
      }
    } else if (elf_pick == 'B') {
      if (you_pick == 'Y') {
        round_score += 3;
      } else if (you_pick == 'Z') {
        round_score += 6;
      }
    } else {
      if (you_pick == 'Z') {
        round_score += 3;
      } else if (you_pick == 'X') {
        round_score += 6;
      }
    }

    total_score += round_score;
    round_score = 0;
  }
  fclose(file);

  printf("The total score for Part 1: %d\n", total_score);
}

void part_2() {
  FILE *file = fopen("inputs/day_2_input.txt", "r");
  char line[1000];
  int total_score = 0;

  while (fgets(line, sizeof(line), file) != NULL) {
    int round_score = 0;
    char elf_pick = line[0];
    char you_pick = line[2];

    if (you_pick == 'X') {
      if (elf_pick == 'A') {
        round_score += 3;
      } else if (elf_pick == 'B') {
        round_score += 1;
      } else {
        round_score += 2;
      }
    } else if (you_pick == 'Y') {
      if (elf_pick == 'A') {
        round_score += 4;
      } else if (elf_pick == 'B') {
        round_score += 5;
      } else {
        round_score += 6;
      }
    } else {
      if (elf_pick == 'A') {
        round_score += 8;
      } else if (elf_pick == 'B') {
        round_score += 9;
      } else {
        round_score += 7;
      }
    }

    total_score += round_score;
    round_score = 0;
  }
  fclose(file);

  printf("The total score for Part 2: %d\n", total_score);
}
