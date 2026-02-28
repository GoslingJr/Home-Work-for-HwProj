#include <stdio.h>

int main() {
    int limit = 1000000;
    int a = 1, b = 1, c;
    long long sum = 0;

    while (b <= limit) {
        if (b % 2 == 0) {
            sum += b;
        }
        c = a + b;
        a = b;
        b = c;
    }

    printf("The sum of the even Fibonacci numbers up to %d: %lld\n", limit, sum);

    return 0;
}