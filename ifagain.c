#include <stdio.h>

int main(){

    double hours, rate, regpay, ovtpay,grosspay,ovt;
    printf("Hours Worked, and Overtime: ");
    scanf("%lf, %lf", &hours, &ovt);
    /*printf("How many overtime hours were worked? ");
    scanf("%lf",&ovt);*/
    printf("Rate of pay? ");
    scanf("%lf", &rate);
    if(hours <= 40){
        regpay = hours * rate;
        ovtpay = 0;
    }
    else{
        regpay =  40 * rate;
        ovtpay = (ovt) * rate * 1.5;
    }
    grosspay = regpay + ovtpay;
    printf("\nRegular pay is : $%3.2f\n",regpay);
    printf("Overtime pay is: $%3.2f\n",ovtpay);
    printf("Gross pay is: $%3.2f\n", grosspay);
}