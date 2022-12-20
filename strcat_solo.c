#include <stdio.h>
#include <string.h>

int main(){

    char attempt[30] = "Joker";
    char murda[15] = " Batman";
/*when using the strcat you cant break the data down(you can just call joker)
so the question is. is it really worth it? how bout i just make a new variable for it*/
    strcat(attempt, murda);

    printf("%s\n", attempt);

    printf("%s\n", murda);

}
