#include <stdio.h>
#include <string.h>

int main(){

    char sum[5];
    char name[50];
    char input[5];

    strcpy(sum, "Yo");

    printf("%s, What is your name? \n", sum);
    gets(name);
    printf("Nice to meet you, %s", name);

    printf("Lets test this, Enter Yes or No"
    "(This is Case-Sentive)\n");
    gets(input);
    
    if (input == "Yes") {printf("Yes\n");}
        else {printf("No\n");}
}