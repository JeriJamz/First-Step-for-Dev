#include <stdio.h>

int main(){

    int a,b,c;// add the semi
    
    a = 13;
    b = a + 12;
    printf("%d %d\n", a,b);
    c = a + b;
    a = a + 11;
    printf("a = %d b = %d c = %d\n", a,b,c);

}