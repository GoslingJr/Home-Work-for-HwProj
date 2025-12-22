#include <stdio.h>

int main() {
    int count = 0;
    int num;
    char ch;

    printf("Enter numbers: ");

    do {
        scanf_s("%d", &num);
        if (num == 0) {
            count++;
        }
        ch = getchar();
    } while (ch != '\n' && ch != EOF);

    printf("Zero elements: %d\n", count);
    return 0;
}