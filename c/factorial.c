// To find factorial of a number

#include<stdio.h>
int main()
{
	int n,i,fact=1;
	printf("enter the number = ");
	scanf("%d",&n);
	for(i=n;i>=1;i--)
	{
	fact=fact*i;

	printf("\nr = %d",fact);
}
printf("\n\n\nfinal result = %d",fact);
	return 0;
}
