#include <stdio.h>

int main(){

    int a,b,c;

    printf("This will help you find the avg or mean\n");
    printf("Please enter a number: ");
    scanf("%d",&a);
    printf("Please enter another number: ");
    scanf("%d", &b);
    printf("Enter the last number: ");
    scanf("%d",&c);

    int average;
    average = (a+b+c)/3;
    printf("The average(mean is), %d", average);

}