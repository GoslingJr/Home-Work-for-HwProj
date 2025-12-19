#include <stdio.h>

int main() {
    int bits[32] = { 0 };
    int n = 0;

    printf("Enter binary digits separated by spaces: ");

    char buffer[100];
    fgets(buffer, sizeof(buffer), stdin);

    char* ptr = buffer;
    int bit;
    while (sscanf_s(ptr, "%d", &bit) == 1) {
        bits[n++] = bit;
        while (*ptr != ' ' && *ptr != '\0' && *ptr != '\n') ptr++;
        while (*ptr == ' ') ptr++;
        if (n >= 32) break;
    }

    unsigned int max_value = 0;

    for (int start = 0; start < n; start++) {
        unsigned int value = 0;

        for (int i = 0; i < n; i++) {
            int index = (start + i) % n;
            value = (value << 1) | bits[index];
        }

        if (value > max_value) {
            max_value = value;
        }
    }

    printf("%u\n", max_value);
    return 0;
}