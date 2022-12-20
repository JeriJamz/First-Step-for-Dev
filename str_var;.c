#include <stdio.h>//this is for printf
#include <string.h>//strcpy is for strcpy

int main(){

    char name[50];//this declares the variable with a max of 50

    strcpy(name, "Alice Wonders");// this set the variable

    printf("Hello, %s\n",name);// dont forget the variable name too

}