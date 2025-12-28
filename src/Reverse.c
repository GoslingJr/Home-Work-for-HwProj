#include <stdio.h>

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    int m, n;
    printf("Enter the lengths of beginning and end separated by space: ");
    scanf_s("%d %d", &m, &n);

    int total = m + n;
    int arr[100];

    printf("Enter %d array elements: ", total);
    for (int i = 0; i < total; i++) {
        scanf_s("%d", &arr[i]);
    }

    int d = gcd(m, n);

    for (int i = 0; i < d; i++) {
        int temp = arr[i];
        int j = i;
        int next;

        while (1) {
            next = (j + m) % total;
            if (next == i) break;
            arr[j] = arr[next];
            j = next;
        }
        arr[j] = temp;
    }

    printf("Result: ");
    for (int i = 0; i < total; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
