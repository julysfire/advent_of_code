#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int comp(const void *a, const void *b) { return (*(int *)a - *(int *)b); }

void part_1() {
  FILE *file = fopen("inputs/day_2_input.txt", "r");

  char line[13];
  int l = 0;
  int w = 0;
  int h = 0;
  int numCounter = 0;
  int surfaceArea = 0;
  int slack = 0;
  int totalDims = 0;

  while (fgets(line, sizeof(line), file) != NULL) {
    char *tok = strtok(line, "x");

    while (tok != NULL) {
      if (numCounter == 0) {
        l = atoi(tok);
      } else if (numCounter == 1) {
        w = atoi(tok);
      } else if (numCounter == 2) {
        h = atoi(tok);
      }

      numCounter += 1;
      tok = strtok(NULL, "x");
    }

    numCounter = 0;

    // l = 0, w = 1, h = 2
    surfaceArea = (2 * l * w) + (2 * w * h) + (2 * l * h);

    if (((l * w) <= (w * h)) && ((l * w) <= (l * h))) {
      slack = l * w;
    } else if (((w * h) <= (l * w)) && ((w * h) <= (l * h))) {
      slack = w * h;
    } else if (((l * h) <= (l * w)) && ((l * h) <= (w * h))) {
      slack = l * h;
    }

    totalDims = totalDims + surfaceArea + slack;
  }

  fclose(file);

  printf("The final total dimensions for Part 1: %d.\n", totalDims);
}

void part_2() {
  FILE *file = fopen("inputs/day_2_input.txt", "r");

  char line[13];
  int l = 0;
  int w = 0;
  int h = 0;
  int numCounter = 0;
  int totalDims = 0;
  int bow = 0;

  while (fgets(line, sizeof(line), file) != NULL) {
    char *tok = strtok(line, "x");

    while (tok != NULL) {
      if (numCounter == 0) {
        l = atoi(tok);
      } else if (numCounter == 1) {
        w = atoi(tok);
      } else if (numCounter == 2) {
        h = atoi(tok);
      }

      numCounter += 1;
      tok = strtok(NULL, "x");
    }

    numCounter = 0;

    bow = l * w * h;

    int lwh[] = {l, w, h};
    int n = sizeof(lwh) / sizeof(lwh[0]);
    qsort(lwh, n, sizeof(lwh[0]), comp);
    int ribbon = lwh[0] + lwh[0] + lwh[1] + lwh[1];

    totalDims = totalDims + ribbon + bow;
  }

  printf("The total dimensions for Part 2 is: %d\n", totalDims);
}

int main() {
  part_1();
  part_2();
}

/*
printf("l w h: %d %d %d\n", l, w, h);
printf("surfaceArea: %d\n", surfaceArea);
printf("slack: %d\n", slack);
printf("\n");
fprintf(o_file, "l w h: %d %d %d\nsurfaceArea: %d\nslack: %d\n\n", l, w, h,
        surfaceArea, slack);
 */
