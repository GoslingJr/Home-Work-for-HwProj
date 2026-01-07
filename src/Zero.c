#include <stdio.h>

int main() {
    int arr[1000];
    int count = 0;

    printf("Enter array elements (enter any non-numeric value to stop):\n");

    int i = 0;
    while (scanf_s("%d", &arr[i]) == 1) {
        if (arr[i] == 0) {
            count++;
        }
        i++;
    }

    printf("Number of zero elements: %d\n", count);

    return 0;
}
