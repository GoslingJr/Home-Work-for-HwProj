#include <stdio.h>

int main() {
    int count[28] = { 0 };
    int total = 0;

    for (int i = 0; i <= 999; i++) {
        int sum = (i / 100) + ((i / 10) % 10) + (i % 10);
        count[sum]++;
    }

    for (int i = 0; i < 28; i++) {
        total += count[i] * count[i];
    }

    printf("%d\n", total);
    return 0;
}
