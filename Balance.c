#include <stdio.h>
#include <string.h>

int main() {
    char str[1000];
    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);

    int balance = 0;
    int length = strlen(str);

    for (int i = 0; i < length; i++) {
        if (str[i] == '(') {
            balance++;
        }
        else if (str[i] == ')') {
            balance--;
            if (balance < 0) {
                printf("NO\n");
                return 0;
            }
        }
    }

    if (balance == 0) {
        printf("YES\n");
    }
    else {
        printf("NO\n");
    }

    return 0;
}