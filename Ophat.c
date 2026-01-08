#include <stdio.h>

int main() {
    int a, b;
    scanf_s("%d %d", &a, &b);

    if (b == 0) {
        printf("Division by zero!\n");
        return 1;
    }

    int q = 0;
    int r = a;

    if (b > 0) {
        while (r >= b) {
            r -= b;
            q++;
        }
        while (r < 0) {
            r += b;
            q--;
        }
    }
    else {
        while (r <= b) {
            r -= b;
            q++;
        }
        while (r > 0) {
            r -= b;
            q--;
        }
    }

    printf("%d\n", q);
    return 0;
}
