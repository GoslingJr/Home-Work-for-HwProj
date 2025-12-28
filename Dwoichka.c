#include <stdio.h>
#include <stdlib.h>

void print_binary(int num, int bits) {
    if (bits == 0) bits = 32;

    for (int i = bits - 1; i >= 0; i--) {
        printf("%d", (num >> i) & 1);
        if (i % 4 == 0 && i != 0) printf(" ");
    }
    printf("\n");
}

void add_binary(int a, int b, int bits) {
    if (bits == 0) bits = 32;

    printf("  ");
    print_binary(a, bits);
    printf("+ ");
    print_binary(b, bits);
    printf("  ");
    for (int i = 0; i < bits + (bits / 4 - 1); i++) printf("-");
    printf("\n");

    int sum = a + b;
    printf("  ");
    print_binary(sum, bits);
}

int main() {
    int a, b;
    scanf_s("%d %d", &a, &b);

    int bits = 8;
    if (abs(a) > 127 || abs(b) > 127 || abs(a + b) > 127) bits = 16;
    if (abs(a) > 32767 || abs(b) > 32767 || abs(a + b) > 32767) bits = 32;

    printf("First number in decimal: %d\n", a);
    printf("First number in binary:\n", bits);
    print_binary(a, bits);
    printf("\n");

    printf("Second number in decimal: %d\n", b);
    printf("Second number in binary:\n", bits);
    print_binary(b, bits);
    printf("\n");

    printf("Binary addition:\n");
    add_binary(a, b, bits);
    printf("\n");

    int sum = a + b;
    printf("Sum in decimal: %d\n", sum);
    printf("Sum in binary: ");
    print_binary(sum, bits);

    return 0;
}
