#include <stdio.h>
int main() {
    int i, n, t1 = 0, t2 = 1, nextTerm;
    printf("Enter the number of terms: ");
    scanf("%d", &n);
    printf("Fibonacci Series: ");


    if(n==1)
        printf("%d, ", t1);
    else if(n==2)
    {
        printf("%d ",t1 );
        printf("%d, ", t2);
    }
    else
    {
       for (i = 1; i <= n; ++i) {
        printf("%d, ", t1);
        nextTerm = t1 + t2;
        t1 = t2;
        t2 = nextTerm;
    }

}


return 0;
}
