#include <stdio.h>

int main(){

    int a,b;

    printf("Enter first number: ");
    scanf("%d", &a);// sacnf is where i can get user input
    printf("Enter second number: ");
    scanf("%d", &b);// scanf in this case only accept int any other num cause sweet 16 error
    printf("%d + %d = %d\n", a,b,a + b);

}