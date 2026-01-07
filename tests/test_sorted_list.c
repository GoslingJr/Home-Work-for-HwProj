#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Node {
    int value;
    struct Node* next;
};

extern struct Node* head;
extern void insert_sorted(int val);
extern void delete_value(int val);
extern void print_list();

int get_list_size() {
    int size = 0;
    struct Node* current = head;
    while (current != NULL) {
        size++;
        current = current->next;
    }
    return size;
}

int is_value_in_list(int val) {
    struct Node* current = head;
    while (current != NULL) {
        if (current->value == val) return 1;
        current = current->next;
    }
    return 0;
}

int is_list_sorted() {
    if (head == NULL || head->next == NULL) return 1;
    
    struct Node* current = head;
    while (current->next != NULL) {
        if (current->value > current->next->value) return 0;
        current = current->next;
    }
    return 1;
}

void free_list() {
    while (head != NULL) {
        struct Node* temp = head;
        head = head->next;
        free(temp);
    }
}

void test_empty_list() {
    printf("Test 1: Empty list\n");
    if (head == NULL && get_list_size() == 0) {
        printf("PASS\n");
    } else {
        printf("FAIL\n");
        exit(1);
    }
}

void test_insert_single() {
    printf("\nTest 2: Insert single element\n");
    free_list();
    insert_sorted(42);
    if (get_list_size() == 1 && is_value_in_list(42) && is_list_sorted()) {
        printf("PASS\n");
    } else {
        printf("FAIL\n");
        exit(1);
    }
}

void test_insert_multiple() {
    printf("\nTest 3: Insert multiple elements\n");
    free_list();
    insert_sorted(30);
    insert_sorted(10);
    insert_sorted(20);
    
    if (get_list_size() == 3 && is_value_in_list(10) && 
        is_value_in_list(20) && is_value_in_list(30) && is_list_sorted()) {
        printf("PASS\n");
    } else {
        printf("FAIL\n");
        exit(1);
    }
}

void test_insert_duplicates() {
    printf("\nTest 4: Insert duplicates\n");
    free_list();
    insert_sorted(5);
    insert_sorted(5);
    insert_sorted(5);
    
    if (get_list_size() == 3 && is_list_sorted()) {
        printf("PASS\n");
    } else {
        printf("FAIL\n");
        exit(1);
    }
}

void test_insert_negative() {
    printf("\nTest 5: Insert negative numbers\n");
    free_list();
    insert_sorted(-5);
    insert_sorted(10);
    insert_sorted(-10);
    
    if (get_list_size() == 3 && is_list_sorted()) {
        printf("PASS\n");
    } else {
        printf("FAIL\n");
        exit(1);
    }
}

void test_delete_existing() {
    printf("\nTest 6: Delete existing element\n");
    free_list();
    insert_sorted(10);
    insert_sorted(20);
    insert_sorted(30);
    
    delete_value(20);
    if (get_list_size() == 2 && !is_value_in_list(20) && 
        is_value_in_list(10) && is_value_in_list(30) && is_list_sorted()) {
        printf("PASS\n");
    } else {
        printf("FAIL\n");
        exit(1);
    }
}

void test_delete_nonexistent() {
    printf("\nTest 7: Delete non-existent element\n");
    free_list();
    insert_sorted(10);
    insert_sorted(20);
    
    int size_before = get_list_size();
    delete_value(99);
    int size_after = get_list_size();
    
    if (size_before == size_after && is_list_sorted()) {
        printf("PASS\n");
    } else {
        printf("FAIL\n");
        exit(1);
    }
}

void test_delete_from_empty() {
    printf("\nTest 8: Delete from empty list\n");
    free_list();
    delete_value(10);
    
    if (head == NULL && get_list_size() == 0) {
        printf("PASS\n");
    } else {
        printf("FAIL\n");
        exit(1);
    }
}

void test_delete_first() {
    printf("\nTest 9: Delete first element\n");
    free_list();
    insert_sorted(10);
    insert_sorted(20);
    insert_sorted(30);
    
    delete_value(10);
    if (get_list_size() == 2 && !is_value_in_list(10) && is_list_sorted()) {
        printf("PASS\n");
    } else {
        printf("FAIL\n");
        exit(1);
    }
}

void test_delete_last() {
    printf("\nTest 10: Delete last element\n");
    free_list();
    insert_sorted(10);
    insert_sorted(20);
    insert_sorted(30);
    
    delete_value(30);
    if (get_list_size() == 2 && !is_value_in_list(30) && is_list_sorted()) {
        printf("PASS\n");
    } else {
        printf("FAIL\n");
        exit(1);
    }
}

void test_all_operations() {
    printf("\nTest 11: All operations combined\n");
    free_list();
    insert_sorted(50);
    insert_sorted(30);
    insert_sorted(70);
    delete_value(30);
    insert_sorted(40);
    insert_sorted(60);
    delete_value(70);
    
    if (get_list_size() == 3 && is_list_sorted()) {
        printf("PASS\n");
    } else {
        printf("FAIL\n");
        exit(1);
    }
}

int main(int argc, char* argv[]) {
    if (argc == 2 && strcmp(argv[1], "--test") == 0) {
        printf("=== Running Sorted List Tests ===\n\n");
        
        test_empty_list();
        test_insert_single();
        test_insert_multiple();
        test_insert_duplicates();
        test_insert_negative();
        test_delete_existing();
        test_delete_nonexistent();
        test_delete_from_empty();
        test_delete_first();
        test_delete_last();
        test_all_operations();
        
        printf("\n=== All tests passed! ===\n");
        free_list();
        return 0;
    }
    
    printf("Run with --test flag to execute tests\n");
    return 0;
}
