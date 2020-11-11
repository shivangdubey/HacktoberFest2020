#include <stdio.h>
int main() {
    int i, n, a1 = 0, a2 = 1, nextTerm;
    printf("Enter the number of terms: ");
    scanf("%d", &n);
    printf("Fibonacci Series: ");


    if(n==1)
        printf("%d, ", a1);
    else if(n==2)
    {
        printf("%d ",a1 );
        printf("%d, ", a2);
    }
    else
    {
       for (i = 1; i <= n; ++i) {
        printf("%d, ", a1);
        nextTerm = a1 + a2;
        a1 = a2;
        a2 = nextTerm;
    }

}


return 0;
}
