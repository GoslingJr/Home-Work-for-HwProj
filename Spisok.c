#include <stdio.h>
#include <stdlib.h>

struct Node {
    int value;
    struct Node* next;
};

struct Node* head = NULL;

void print_list() {
    if (head == NULL) {
        printf("List is empty\n");
        return;
    }

    struct Node* current = head;
    while (current != NULL) {
        printf("%d ", current->value);
        current = current->next;
    }
    printf("\n");
}

void insert_sorted(int val) {
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->value = val;
    new_node->next = NULL;

    if (head == NULL || val < head->value) {
        new_node->next = head;
        head = new_node;
        return;
    }

    struct Node* current = head;
    while (current->next != NULL && current->next->value < val) {
        current = current->next;
    }

    new_node->next = current->next;
    current->next = new_node;
}

void delete_value(int val) {
    if (head == NULL) return;

    if (head->value == val) {
        struct Node* temp = head;
        head = head->next;
        free(temp);
        return;
    }

    struct Node* current = head;
    while (current->next != NULL && current->next->value != val) {
        current = current->next;
    }

    if (current->next != NULL) {
        struct Node* temp = current->next;
        current->next = current->next->next;
        free(temp);
    }
}

int main() {
    int choice, value;

    while (1) {
        printf("\nMenu:\n");
        printf("0 - Exit\n");
        printf("1 - Add value to sorted list\n");
        printf("2 - Delete value from list\n");
        printf("3 - Print list\n");
        printf("Your choice: ");
        scanf_s("%d", &choice);

        switch (choice) {
        case 0:
            return 0;
        case 1:
            printf("Enter value to add: ");
            scanf_s("%d", &value);
            insert_sorted(value);
            printf("Value %d added\n", value);
            break;
        case 2:
            printf("Enter value to delete: ");
            scanf_s("%d", &value);
            delete_value(value);
            printf("Value %d deleted (if existed)\n", value);
            break;
        case 3:
            printf("Current list: ");
            print_list();
            break;
        default:
            printf("Invalid choice\n");
        }
    }

    return 0;
}