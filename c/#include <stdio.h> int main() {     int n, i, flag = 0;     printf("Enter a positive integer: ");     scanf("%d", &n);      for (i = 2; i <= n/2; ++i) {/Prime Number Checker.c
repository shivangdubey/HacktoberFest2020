#include <stdio.h> 
#include<math.h> 
int main() 
{ 
	int n, i, flag = 1; 

	// Ask user for input 
	printf("Enter a number: \n"); 

	// Store input number in a variable 
	scanf("%d", &n); 

	// Iterate from 2 to n/2 
	for (i = 2; i <= sqrt(n); i++) { 

		// If n is divisible by any number between 
		// 2 and n/2, it is not prime 
		if (n % i == 0) { 
			flag = 0; 
			break; 
		} 
	} 

	if(n<=1) 
	flag=0; 
	else if(n==2) 
	flag=1; 

	if (flag == 1) { 
		printf("%d is a prime number", n); 
	} 
	else { 
		printf("%d is not a prime number", n); 
	} 

	return 0; 
} 

/*A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself.*/
/*The idea to make this code is to iterate through all the numbers starting from 2 to sqrt(N) using a for loop and for every number check if it divides N.
If we find any number that divides, we return false. 
If we did not find any number between 2 and sqrt(N) which divides N then it means that N is prime and we will return True.

Why did we choose sqrt(N)?
The reason is that the smallest and greater than one factor of a number cannot be more than the sqrt of N. And we stop as soon as we find a factor. */
