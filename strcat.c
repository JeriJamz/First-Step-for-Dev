#include <stdio.h>
#include <string.h>

int main(){

    char name[30] = "Alice";
    char last[15] = "Wonderland";
    char joke[30];

    strcat(name, last);// strcat means string concatination
    strcpy(joke, "True");


    printf("%s, %s\n"
    "%s\n"
    "%s\n", name, last, name, joke);

}