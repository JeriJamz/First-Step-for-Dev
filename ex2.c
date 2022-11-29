#include <stdio.h>
#include <float.h>

int main(){
    printf("Storage size for int: %d \n", sizeof(int));//were starting to get advance boys. so this operator finds the size of somethings
    printf("Storage size for float: %d \n", sizeof(float));
    printf("Minimum float postive value: %E\n", FLT_MIN);
    printf("Maximum float postive value: %E\n", FLT_MAX);
    printf("Precision value: %d\n", FLT_DIG);
    printf("Storage size for double: %d \n", sizeof(double));
    printf("Storage size for long double: %d \n", sizeof(long double));
    return 0;
}