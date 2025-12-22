#include <stdio.h>

int main() {
    int a, b;
    scanf_s("%d %d", &a, &b);

    if (b == 0) {
        printf("Division by zero!\n");
        return 1;
    }

    int quotient = 0;
    int sign = 1;

    if ((a >= 0 && b > 0) || (a < 0 && b < 0)) {
        sign = 1;
    }
    else {
        sign = -1;
    }

    int abs_a = a;
    int abs_b = b;

    if (abs_a < 0) abs_a = -abs_a;
    if (abs_b < 0) abs_b = -abs_b;

    int temp = abs_b;

    while (temp <= abs_a) {
        temp += abs_b;
        quotient++;
    }

    printf("%d\n", sign * quotient);
    return 0;
}