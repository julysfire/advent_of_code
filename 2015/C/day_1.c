#include <stdio.h>

void part_1() {
  FILE *file = fopen("inputs/day_1_input.txt", "r");

  char line[1000];
  char indvChar = '(';
  int counter = 0;

  // Read the line into the buffer, 1000 length at a time
  while (fgets(line, sizeof(line), file) != NULL) {
    // For each character, where line is != '\0\' which is the null terminator
    // This will keep the buffer moving
    for (int i = 0; line[i] != '\0'; i++) {
      indvChar = line[i];

      if (indvChar == '(') {
        counter += 1;
      } else if (indvChar == ')') {
        counter -= 1;
      }
    }
  }
  fclose(file);

  printf("The result Floor is %d.\n", counter);
}
void part_2() {
  FILE *file = fopen("inputs/day_1_input.txt", "r");
  char indvChar = '(';
  int counter = 0;
  int posCounter = 0;

  // Read individual char at a time
  while ((indvChar = fgetc(file)) != EOF) {
    if (indvChar == '(') {
      counter += 1;
      posCounter += 1;
    } else if (indvChar == ')') {
      counter -= 1;
      posCounter += 1;
    }

    if (counter < 0) {
      break;
    }
  }
  fclose(file);

  printf("The position where Santa first entered the basement was %d.\n",
         posCounter);
}

int main() {
  part_1();
  part_2();
}
