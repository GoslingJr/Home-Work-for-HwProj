#include <stdio.h>
#include <stdlib.h>

struct Node {
    int position;
    struct Node* next;
};

int main() {
    int n, m;
    scanf_s("%d %d", &n, &m);

    if (n <= 0 || m <= 0) {
        printf("Invalid input\n");
        return 1;
    }

    struct Node* head = malloc(sizeof(struct Node));
    head->position = 1;
    head->next = head;

    struct Node* current = head;

    for (int i = 2; i <= n; i++) {
        struct Node* new_node = malloc(sizeof(struct Node));
        new_node->position = i;
        new_node->next = head;

        current->next = new_node;
        current = new_node;
    }

    struct Node* prev = current;
    current = head;

    while (current->next != current) {
        for (int i = 1; i < m; i++) {
            prev = current;
            current = current->next;
        }

        prev->next = current->next;
        struct Node* to_free = current;
        current = current->next;
        free(to_free);
    }

    printf("%d\n", current->position);
    free(current);

    return 0;
}
