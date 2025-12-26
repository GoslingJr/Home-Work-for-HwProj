#include <stdio.h>

int main() {
    int a, b;
    scanf_s("%d %d", &a, &b);

    if (b == 0) {
        printf("Division by zero!\n");
        return 1;
    }

    int q = 0;

    int pos_b = b;
    if (pos_b < 0) pos_b = -pos_b;

    int pos_a = a;
    if (pos_a < 0) pos_a = -pos_a;

    int temp = 0;
    while (temp + pos_b <= pos_a) {
        temp += pos_b;
        q++;
    }

    if ((a >= 0 && b > 0) || (a < 0 && b < 0)) {
        printf("%d\n", q);
    }
    else {
        printf("%d\n", -q);
    }

    return 0;
}