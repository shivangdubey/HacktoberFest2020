#include <stdio.h>
#include <math.h>

#define BASE 2

int main()
{
    long long binary, decimal=0, tempBinary;
    int N=0;

    printf("Enter any binary number: ");
    scanf("%lld", &binary);

    tempBinary = binary;

    while(tempBinary!=0)
    {
        /* If current binary digit is 1 */
        if(tempBinary % 10 == 1)
        {
            decimal += pow(BASE, N);
        }

        N++;
        tempBinary /= 10;
    }

    printf("Binary number = %lld\n", binary);
    printf("Decimal number= %lld", decimal);

    return 0;
}
