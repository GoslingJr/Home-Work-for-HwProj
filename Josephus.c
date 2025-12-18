#include <stdio.h>

int josephus(int n, int m) {
    int result = 0;
    for (int i = 2; i <= n; i++) {
        result = (result + m) % i;
    }
    return result + 1;
}

int main() {
    int n, m;
    printf("Enter number of warriors (n): ");
    scanf_s("%d", &n);
    printf("Enter kill every m-th warrior: ");
    scanf_s("%d", &m);

    int survivor = josephus(n, m);
    printf("Survivor position: %d\n", survivor);

    return 0;
}