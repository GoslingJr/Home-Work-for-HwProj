#include <stdio.h>

char s[1000];
int t = -1;

int main() {
    char str[1000];
    fgets(str, sizeof(str), stdin);

    for (int i = 0; str[i]; i++) {
        char c = str[i];
        if (c == '(' || c == '[' || c == '{') {
            s[++t] = c;
        }
        else if (c == ')' && (t == -1 || s[t--] != '(')) {
            printf("NO\n");
            return 0;
        }
        else if (c == ']' && (t == -1 || s[t--] != '[')) {
            printf("NO\n");
            return 0;
        }
        else if (c == '}' && (t == -1 || s[t--] != '{')) {
            printf("NO\n");
            return 0;
        }
    }

    printf(t == -1 ? "YES\n" : "NO\n");
    return 0;
}