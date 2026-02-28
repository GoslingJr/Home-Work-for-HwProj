#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

void gnomeSort(int arr[], int n) {
    int index = 0;

    while (index < n) {
        if (index == 0 || arr[index] >= arr[index - 1]) {
            index++;
        }
        else {
            int temp = arr[index];
            arr[index] = arr[index - 1];
            arr[index - 1] = temp;
            index--;
        }
    }
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int capacity = 10; // Начальная вместимость массива
    int size = 0;      // Текущее количество элементов
    int* arr = (int*)malloc(capacity * sizeof(int));

    if (arr == NULL) {
        printf("Memory allocation failed!\n");
        return 1;
    }

    printf("Enter integers (press Enter after each, type 'q' to finish):\n");

    char input[100];
    while (1) {
        printf("Element %d: ", size + 1);

        // Считываем ввод как строку
        if (scanf("%s", input) != 1) {
            break;
        }

        // Проверяем, не ввели ли 'q' для завершения
        if (input[0] == 'q' || input[0] == 'Q') {
            break;
        }

        // Преобразуем строку в число
        int num;
        if (sscanf(input, "%d", &num) != 1) {
            printf("Invalid input! Enter a number or 'q' to finish.\n");
            continue;
        }

        // Если массив заполнен, увеличиваем его размер
        if (size >= capacity) {
            capacity *= 2;
            int* temp = (int*)realloc(arr, capacity * sizeof(int));
            if (temp == NULL) {
                printf("Memory reallocation failed!\n");
                free(arr);
                return 1;
            }
            arr = temp;
        }

        arr[size] = num;
        size++;
    }

    if (size == 0) {
        printf("No numbers entered!\n");
        free(arr);
        return 0;
    }

    printf("\nYou entered %d numbers.\n", size);
    printf("Original array: ");
    printArray(arr, size);

    gnomeSort(arr, size);

    printf("Sorted array: ");
    printArray(arr, size);

    free(arr);

    return 0;
}