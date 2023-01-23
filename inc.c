#include <stdio.h>

int main(){

    int a,b,c,e,f,g,h,n;
    n = 5;
    a = b = c = 15;
    e = (f=(g = 15));
    h = 15641; //This is the same as h = h + n (Wrks w/ any vari or math oper(+,/,etc))
    h -= 15197;

    printf("Suffix: %d\n"
    "Prefix: %d\n"
    "This some other stuff %d %d %d\n"
    "This some other stuff too %d %d %d\n"
    "Little testy test %d",
    n++, ++n,a,b,c,e,f,g,h );

}