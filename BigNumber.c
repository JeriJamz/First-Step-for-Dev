#include <stdio.h>

int main(){

    int n, bn;
    bn = 0;

    printf("This is supposed to find the biggest number.\n");
    scanf("%d", &n);
    while(n != 0){
        if(n > bn) bn = n;
        scanf("%d", &bn);
    }
    printf("This is the biggest number %d", bn);
}