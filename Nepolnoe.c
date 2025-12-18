#include <stdio.h>

int main() {
    int a, b;
    scanf_s("%d %d", &a, &b);

    int quotient = 0;
    int temp = b;

    if (b > 0) {
        while (temp <= a) {
            temp += b;
            quotient++;
        }
    }
    else if (b < 0) {
        if (a >= 0) {
            while (temp > a) {
                temp += b;
                quotient--;
            }
        }
        else {
            while (temp >= a) {
                temp += b;
                quotient++;
            }
        }
    }
    else {
        quotient = 0;
    }

    printf("%d\n", quotient);
    return 0;
}