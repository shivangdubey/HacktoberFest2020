#include<stdio.h>
int main()
{
	int n,r,a=0,temp;
	printf("Enter the number : ");
	scanf("%d",&n);
	temp = n;
	printf("You entered number : %d\n",n);
	while(n!=0)
	{
		r = n % 10;
		a = a + (r*r*r);
		n /= 10;
	}
	if(a == temp)
	{
		printf("It is a armstrong number");
	}
	else
	{
		printf("It is not a armstrong number");
	}
	return 0;
}
