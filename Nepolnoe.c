#include <stdio.h>

int main() {
    int a, b;

    printf("Enter two integers (a and b, b != 0): ");
    scanf_s("%d %d", &a, &b);

    if (b == 0) {
        printf("Error: Division by zero is not allowed.\n");
        return 1;
    }

    int quotient = 0;
    int remainder = a;

    if (b > 0) {
        if (a >= 0) {
            while (remainder >= b) {
                remainder = remainder - b;
                quotient++;
            }
        }
        else {
            while (remainder < 0) {
                remainder = remainder + b;
                quotient--;
            }
        }
    }
    else {
        int abs_b = -b;

        if (a >= 0) {
            while (remainder >= abs_b) {
                remainder = remainder - abs_b;
                quotient--;
            }
        }
        else {
            while (remainder < 0) {
                remainder = remainder + abs_b;
                quotient++;
            }
        }
    }

    printf("Incomplete quotient: %d\n", quotient);
    printf("Remainder: %d\n", remainder);
    printf("Check: %d = %d * %d + %d\n", a, b, quotient, remainder);

    return 0;
}
