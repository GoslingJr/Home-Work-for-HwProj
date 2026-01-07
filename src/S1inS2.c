#include <stdio.h>

int main() {
    char S[1000], S1[1000];

    printf("Enter string S: ");
    fgets(S, sizeof(S), stdin);

    printf("Enter substring S1: ");
    fgets(S1, sizeof(S1), stdin);

    int count = 0;

    for (int i = 0; S[i] != '\0'; i++) {
        int j = 0;
        int k = i;

        while (S1[j] != '\0' && S1[j] != '\n' && S[k] != '\0') {
            if (S[k] != S1[j]) {
                break;
            }
            k++;
            j++;
        }

        if (S1[j] == '\0' || S1[j] == '\n') {
            count++;
        }
    }

    printf("%d\n", count);

    return 0;
}
