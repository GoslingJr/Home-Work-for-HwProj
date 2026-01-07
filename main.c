#include <stdio.h>

extern int sort_array(int* array, int size);

int main() {
    int array[100];
    int size = 0;
    
    while (size < 100 && scanf("%d", &array[size]) == 1) {
        size++;
    }
    
    int changed_count = sort_array(array, size);
    
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
    
    return changed_count;
}
