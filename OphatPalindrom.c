#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

void add_to_end(struct Node** head, int value) {
    struct Node* new_node = malloc(sizeof(struct Node));
    new_node->data = value;
    new_node->next = NULL;

    if (*head == NULL) {
        *head = new_node;
        return;
    }

    struct Node* current = *head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = new_node;
}

int is_symmetric(struct Node* head) {
    if (head == NULL || head->next == NULL) {
        return 1;
    }

    struct Node* slow = head;
    struct Node* fast = head;
    struct Node* prev = NULL;
    struct Node* temp;

    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;

        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    struct Node* second_half = slow;
    if (fast != NULL) {
        second_half = slow->next;
    }

    struct Node* first_half = prev;

    int result = 1;
    while (first_half != NULL && second_half != NULL) {
        if (first_half->data != second_half->data) {
            result = 0;
            break;
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    return result;
}

int main() {
    struct Node* head = NULL;
    int num;
    printf("Enter numbers: ");

    char buffer[1000];
    fgets(buffer, sizeof(buffer), stdin);

    char* ptr = buffer;
    while (sscanf_s(ptr, "%d", &num) == 1) {
        add_to_end(&head, num);
        while (*ptr != ' ' && *ptr != '\0' && *ptr != '\n') ptr++;
        while (*ptr == ' ') ptr++;
    }

    if (is_symmetric(head)) {
        printf("YES\n");
    }
    else {
        printf("NO\n");
    }

    return 0;
}