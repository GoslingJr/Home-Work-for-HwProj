#include <stdio.h>

int main() {
    double x;
    scanf_s("%lf", &x);

    double x2 = x * x;
    double result = (x2 + 1) * (x2 + x) + 1;

    printf("%lf\n", result);
    return 0;
}
