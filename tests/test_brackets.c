#include <stdio.h>
#include <string.h>

int test_balance(const char* str) {
    char s[1000];
    int t = -1;
    
    for (int i = 0; str[i]; i++) {
        char c = str[i];
        if (c == '(' || c == '[' || c == '{') {
            s[++t] = c;
        }
        else if (c == ')' && (t == -1 || s[t--] != '(')) {
            return 0;
        }
        else if (c == ']' && (t == -1 || s[t--] != '[')) {
            return 0;
        }
        else if (c == '}' && (t == -1 || s[t--] != '{')) {
            return 0;
        }
    }
    return t == -1 ? 1 : 0;
}

int main() {
    printf("Testing brackets...\n");
    
    if (!test_balance("")) {
        printf("FAIL: Empty string\n");
        return 1;
    }
    printf("Empty string\n");
    
    if (!test_balance("()")) {
        printf("FAIL: ()\n");
        return 1;
    }
    if (!test_balance("[]")) {
        printf("FAIL: []\n");
        return 1;
    }
    if (!test_balance("{}")) {
        printf("FAIL: {}\n");
        return 1;
    }
    printf("Simple brackets\n");
    
    if (test_balance("(")) {
        printf("FAIL: (\n");
        return 1;
    }
    if (test_balance(")")) {
        printf("FAIL: )\n");
        return 1;
    }
    if (test_balance("([)]")) {
        printf("FAIL: ([)]\n");
        return 1;
    }
    printf("Unbalanced cases\n");
    
    printf("All tests passed!\n");
    return 0;
}
