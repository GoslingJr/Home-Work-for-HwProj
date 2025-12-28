#include <stdio.h>

char stack[1000];
int top = -1;

int priority(char op) {
    if (op == '+' || op == '-') return 1;
    if (op == '*' || op == '/') return 2;
    return 0;
}

int main() {
    char expr[1000];
    fgets(expr, sizeof(expr), stdin);

    for (int i = 0; expr[i]; i++) {
        char c = expr[i];

        if (c >= '0' && c <= '9') {
            while (expr[i] >= '0' && expr[i] <= '9') {
                putchar(expr[i++]);
            }
            putchar(' ');
            i--;
        }
        else if (c == '(') {
            stack[++top] = c;
        }
        else if (c == ')') {
            while (top >= 0 && stack[top] != '(') {
                putchar(stack[top--]);
                putchar(' ');
            }
            top--;
        }
        else if (c == '+' || c == '-' || c == '*' || c == '/') {
            while (top >= 0 && priority(stack[top]) >= priority(c)) {
                putchar(stack[top--]);
                putchar(' ');
            }
            stack[++top] = c;
        }
    }

    while (top >= 0) {
        putchar(stack[top--]);
        putchar(' ');
    }

    return 0;
}
