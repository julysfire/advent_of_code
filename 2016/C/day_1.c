#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void day_1() {
  // File ops
  FILE *file = fopen("inputs/day_1_input.txt", "r");
  char line[1000];

  // For substring copying
  char dest[9];

  // Day variables
  int heading = 0;
  int loc[] = {0, 0};
  int steps = 0;

  while (fgets(line, sizeof(line), file) != NULL) {
    for (int i = 0; line[i] != '\0'; i++) {
      char *tok = strtok(&line[i], ", ");

      while (tok != NULL) {
        // Update heading
        strncpy(dest, tok + 0, 1);
        // Required null terminator for the string to work properly
        dest[1] = '\0';

        if (strcmp(dest, "L") == 0) {
          heading -= 1;
        } else if (strcmp(dest, "R") == 0) {
          heading += 1;
        }

        // Check wrapping
        if (heading < 0) {
          heading = 3;
        } else if (heading > 3) {
          heading = 0;
        }

        // Move
        strncpy(dest, tok + 1, 9);
        steps = atoi(dest);
        if (steps > 0) {
          if (heading == 0) {
            loc[0] = loc[0] + steps;
          } else if (heading == 1) {
            loc[1] = loc[1] + steps;
          } else if (heading == 2) {
            loc[0] = loc[0] - steps;
          } else if (heading == 3) {
            loc[1] = loc[1] - steps;
          }
        }

        tok = strtok(NULL, ", ");
      }
    }
  }
  fclose(file);

  int valAway = abs(loc[0]) + abs(loc[1]);
  printf("The result location for Part 1 is %d.\n", valAway);
}

void day_2() {
  // File ops
  FILE *file = fopen("inputs/day_1_input.txt", "r");
  char line[1000];

  // For substring copying
  char dest[9];

  // Day variables
  int heading = 0;
  int loc[] = {0, 0};
  int steps = 0;
}

int main() {
  day_1();
  day_2();
}
