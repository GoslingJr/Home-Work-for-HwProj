#include <stdio.h>
#include <string.h>

void get_postfix(const char* expr, char* output) {
    char stack[1000];
    int top = -1;
    int out_idx = 0;
    
    for (int i = 0; expr[i]; i++) {
        char c = expr[i];

        if (c >= '0' && c <= '9') {
            while (expr[i] >= '0' && expr[i] <= '9') {
                output[out_idx++] = expr[i++];
            }
            output[out_idx++] = ' ';
            i--;
        }
        else if (c == '(') {
            stack[++top] = c;
        }
        else if (c == ')') {
            while (top >= 0 && stack[top] != '(') {
                output[out_idx++] = stack[top--];
                output[out_idx++] = ' ';
            }
            top--;
        }
        else if (c == '+' || c == '-' || c == '*' || c == '/') {
            int priority(char op) {
                if (op == '+' || op == '-') return 1;
                if (op == '*' || op == '/') return 2;
                return 0;
            }
            
            while (top >= 0 && priority(stack[top]) >= priority(c)) {
                output[out_idx++] = stack[top--];
                output[out_idx++] = ' ';
            }
            stack[++top] = c;
        }
    }

    while (top >= 0) {
        output[out_idx++] = stack[top--];
        output[out_idx++] = ' ';
    }
    
    output[out_idx] = '\0';
}

int main() {
    printf("Testing calculator...\n");
    
    char output[1000];
    
    get_postfix("1+2", output);
    if (strcmp(output, "1 2 + ") != 0) {
        printf("FAIL: 1+2, got: %s\n", output);
        return 1;
    }
    printf("1+2 -> 1 2 +\n");
    
    get_postfix("2*3", output);
    if (strcmp(output, "2 3 * ") != 0) {
        printf("FAIL: 2*3, got: %s\n", output);
        return 1;
    }
    printf("2*3 -> 2 3 *\n");
    
    get_postfix("(1+2)*3", output);
    if (strcmp(output, "1 2 + 3 * ") != 0) {
        printf("FAIL: (1+2)*3, got: %s\n", output);
        return 1;
    }
    printf("(1+2)*3 -> 1 2 + 3 *\n");
    
    printf("All tests passed!\n");
    return 0;
}
