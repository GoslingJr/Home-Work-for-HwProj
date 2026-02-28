#include <stdio.h>

typedef union {
    double d;
    unsigned long long ull;
} DoubleUnion;

int main() {
    DoubleUnion du;
    
    printf("Enter a number: ");
    scanf("%lf", &du.d);
    
    unsigned long long bits = du.ull;
    
    int sign = (bits >> 63) & 1;
    int exponent = (bits >> 52) & 0x7FF;
    unsigned long long mantissa = bits & 0xFFFFFFFFFFFFF;
    
    double m;
    int p;
    
    if (exponent == 0) {
        if (mantissa == 0) {
            m = 0.0;
            p = 0;
        } else {
            m = mantissa / (double)(1ULL << 52);
            p = -1022;
        }
    } else if (exponent == 0x7FF) {
        printf("Special value (infinity or NaN)\n");
        return 0;
    } else {
        m = 1.0 + mantissa / (double)(1ULL << 52);
        p = exponent - 1023;
    }
    
    printf("Result: %c%.19f*2^%d\n", sign ? '-' : '+', m, p);
    
    return 0;
}
