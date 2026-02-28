#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int isPalindrome(const char* str) {
    size_t left = 0;
    size_t right = strlen(str) - 1;

    while (left < right) {
        while (left < right && str[left] == ' ') {
            left++;
        }

        while (left < right && str[right] == ' ') {
            right--;
        }

        if (str[left] != str[right]) {
            return 0;
        }

        left++;
        right--;
    }

    return 1;
}

int main() {
    char str[1000];
    int choice;

    printf("Choose input method:\n");
    printf("1 - Use example from task\n");
    printf("2 - Enter string manually\n");
    printf("Your choice: ");
    scanf("%d", &choice);

    while (getchar() != '\n');

    if (choice == 1) {
        strcpy(str, "ya idu s mechem sudiya");
        printf("Using string: \"%s\"\n", str);
    }
    else {
        printf("Enter string: ");
        fgets(str, sizeof(str), stdin);

        size_t len = strlen(str);
        if (len > 0 && str[len - 1] == '\n') {
            str[len - 1] = '\0';
        }
    }

    if (isPalindrome(str)) {
        printf("The string is a palindrome.\n");
    }
    else {
        printf("The string is NOT a palindrome.\n");
    }

    return 0;
}