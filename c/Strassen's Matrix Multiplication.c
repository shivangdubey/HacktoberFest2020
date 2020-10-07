/*
STRASSEN'S MATRIX MULTIPLICATION BY SAURABH VERMA
Works upto 64x64 matrix
SAMPLE OUTPUT
-------------
Enter number of rows and columns of first matrix
4 3
Enter elements of first matrix
4 7 1
6 2 7
6 3 2
7 5 9
Enter number of rows and columns of second matrix
3 3
Enter elements of second matrix
9 6 5
8 5 4
1 2 5
Result of A x B
93      61      53
77      60      73
80      55      52
112     85      100
*/

#include<stdio.h>
#define MAX 64
typedef struct mat
{
	int t[MAX][MAX];
}m;
m plus(m a,m b,int n)
{
	int i,j;
	m c;
	for(i=0;i<n;i++)
		for(j=0;j<n;j++)
			c.t[i][j]=a.t[i][j]+b.t[i][j];
	return c;
}
m minus(m a,m b,int n)
{
	int i,j;
	m c;
	for(i=0;i<n;i++)
		for(j=0;j<n;j++)
			c.t[i][j]=a.t[i][j]-b.t[i][j];
	return c;
}
m strass(m a,m b,int n)
{
	m p1,p2,p3,p4,p5,p6,p7,t1,t2,t3,t4,t5,t6,t7,t8,sub1,add1,add2;
	m c;
	int i, j, q;
	if(n==1)
		c.t[0][0] = a.t[0][0]*b.t[0][0];
	else
	{
		q = n/2;
		for(i=0;i<q;i++)
			for(j=0;j<q;j++)
				t1.t[i][j] = a.t[i][j]; 

		for(i=0;i<q;i++)
			for(j=q;j<n;j++)
				t2.t[i][j-q] = a.t[i][j];

		for(i=q;i<n;i++)
			for(j=0;j<q;j++)
				t3.t[i-q][j] = a.t[i][j];

		for(i=q;i<n;i++)
			for(j=q;j<n;j++)
				t4.t[i-q][j-q] = a.t[i][j];

		for(i=0;i<q;i++)
			for(j=0;j<q;j++)
				t5.t[i][j] = b.t[i][j];

		for(i=0;i<q;i++)
			for(j=q;j<n;j++)
				t6.t[i][j-q] = b.t[i][j];

		for(i=q;i<n;i++)
			for(j=0;j<q;j++)
				t7.t[i-q][j] = b.t[i][j];

		for(i=q;i<n;i++)
			for(j=q;j<n;j++)
				t8.t[i-q][j-q] = b.t[i][j];

		sub1 = minus(t6,t8,q);
		p1 = strass(t1,sub1,q);
		add1 = plus(t1,t2,q);
		p2 = strass(add1,t8,q);
		add1 = plus(t3,t4,q);
		p3 = strass(add1,t5,q);
		sub1 = minus(t7,t5,q);
		p4 = strass(t4,sub1,q);
		add1 = plus(t1,t4,q);
		add2 = plus(t5,t8,q);
		p5 = strass(add1,add2,q);
		sub1 = minus(t2,t4,q);
		add1 = plus(t7,t8,q);
		p6 = strass(sub1,add1,q);
		sub1 = minus(t1,t3,q);
		add1 = plus(t5,t6,q);
		p7 = strass(sub1,add1,q);

		for(i=0;i<q;i++)
			for(j=0;j<q;j++)
				c.t[i][j] = p5.t[i][j] + p4.t[i][j] - p2.t[i][j] + p6.t[i][j];

		for(i=0;i<q;i++)
			for(j=0;j<q;j++)
				c.t[i][j+q] = p1.t[i][j] + p2.t[i][j];

		for(i=0;i<q;i++)
			for(j=0;j<q;j++)
				c.t[i+q][j] = p3.t[i][j] + p4.t[i][j];

		for(i=0;i<q;i++)
			for(j=0;j<q;j++)
				c.t[i+q][j+q] = p1.t[i][j] + p5.t[i][j] - p3.t[i][j] - p7.t[i][j];
	}
	return c;
}
int main()
{
	int in[4];
	int i,j,k=0,n=1;
	m m1,m2,m3;

	printf("Enter number of rows and columns of first matrix\n");
    scanf("%d%d", &in[0], &in[1]);
    printf("Enter elements of first matrix\n");
	for (i = 0; i < in[0]; i++)
    	for (j = 0; j < in[1]; j++)
      		scanf("%d", &m1.t[i][j]);

    printf("\nEnter number of rows and columns of second matrix\n");
	while(1)
	{
		scanf("%d%d", &in[2], &in[3]);
		if(in[1]==in[2])
			break;
		printf("\n**ENTER VALID DIMENSIONS**\n");
	}
	printf("Enter elements of second matrix\n");
	for (i = 0; i < in[2]; i++)
		for (j = 0; j < in[3]; j++)
			scanf("%d", &m2.t[i][j]);
	
	for(i=0;i<4;i++)
		if(in[i]>k)
			k=in[i];

	while(1)
	{
		if(n>=k)
			break;
		n*=2;
	}
	m3 = strass(m1,m2,n);
	printf("\nResult of A x B\n");
	for(i=0;i<in[0];i++)
	{
		for(j=0;j<in[3];j++)
			printf("%d\t",m3.t[i][j]);
		printf("\n");
	}
	return 0;
}