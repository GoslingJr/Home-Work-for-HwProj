#include <stdio.h>
#include <stdlib.h>

typedef struct ListNode {
    int value;
    struct ListNode* next;
} ListNode;

typedef struct Queue {
    ListNode* f;
    ListNode* r;
} Queue;

ListNode* create_node(int value) {
    ListNode* node = (ListNode*)malloc(sizeof(ListNode));
    node->value = value;
    node->next = NULL;
    return node;
}

void free_list(ListNode* list) {
    while (list) {
        ListNode* temp = list;
        list = list->next;
        free(temp);
    }
}

void push_front(ListNode** list, int value) {
    ListNode* node = create_node(value);
    node->next = *list;
    *list = node;
}

void transfer(ListNode** from, ListNode** to) {
    if (*from == NULL) return;
    ListNode* temp = *from;
    *from = NULL;
    while (temp) {
        ListNode* next = temp->next;
        temp->next = *to;
        *to = temp;
        temp = next;
    }
}

void enqueue(Queue* q, int value) {
    push_front(&(q->r), value);
}

int dequeue(Queue* q, int* result) {
    if (q->f == NULL) {
        transfer(&(q->r), &(q->f));
        q->r = NULL;
    }
    if (q->f == NULL) {
        return 0;
    }
    ListNode* temp = q->f;
    *result = temp->value;
    q->f = q->f->next;
    free(temp);
    return 1;
}

void init_queue(Queue* q) {
    q->f = NULL;
    q->r = NULL;
}

void free_queue(Queue* q) {
    free_list(q->f);
    free_list(q->r);
}

int main() {
    Queue q;
    init_queue(&q);

    printf("Test 1: Enqueue 1, 2, 3 and dequeue all\n");
    enqueue(&q, 1);
    enqueue(&q, 2);
    enqueue(&q, 3);
    int val;
    while (dequeue(&q, &val)) {
        printf("%d ", val);
    }
    printf("\n");

    printf("Test 2: Enqueue 4, 5 and dequeue all\n");
    enqueue(&q, 4);
    enqueue(&q, 5);
    while (dequeue(&q, &val)) {
        printf("%d ", val);
    }
    printf("\n");

    printf("Test 3: Dequeue from empty queue\n");
    if (!dequeue(&q, &val)) {
        printf("Queue is empty\n");
    }
    printf("\n");

    printf("Test 4: Enqueue 6, 7, 8 and dequeue all\n");
    enqueue(&q, 6);
    enqueue(&q, 7);
    enqueue(&q, 8);
    while (dequeue(&q, &val)) {
        printf("%d ", val);
    }
    printf("\n");

    free_queue(&q);
    return 0;
}