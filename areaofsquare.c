#include <stdio.h>

int main(){
    int a, s;
    printf("Enter length of side: ");
    scanf("%d", &s);// store the length in s
    a = s * s; // caluclate area; store in a
    printf("\nArea of square is %d\n", a);// this is the final output
}