#include<stdio.h>
#include<stdlib.h>
void main()
{ 
	int min(int,int);
	int n,key,arr[30],i,j,a=0,b=1,c,fib[30],fibm,m1,m2,index,v,offset=0;
	printf("enter n & key values:");
	scanf("%d%d",&n,&key);
	printf("enter %d elements",n);
	for(i=0;i<n;i++)
	{
		scanf("%d",&arr[i]);
	}
	fib[0]=0,fib[1]=1;
	for(j=2;j<n+5;j++)
	{
		c=a+b;
		a=b;
		b=c;
		fib[j]=c;
	}
	for(v=0;v<n+5;v++)
	{
		if(fib[v]>=n)
		  break;
	}
	fibm=fib[v];
	m1=fib[v-1];
	m2=fib[v-2];
	int k=0,f=0;
	
	while(k<=n+1)
	{
		int z=offset+m2;
		index=min(z,n);
		if(arr[index]==key)
		{
			printf("element found at %d position",index+1);
			f=1;
			break;
		}
		else if(arr[index]<key)
		{
			fibm=fib[v-1];
			m1=fib[v-2];
			m2=fib[v-3];
			offset=index;
			v=v-1;
		}
		else
		{
		     fibm=fib[v-2];
			 m1=fib[v-3];
			 m2=fib[v-4];		
			 v=v-2;
			
		}
		k++;
		
	}
	if(f==0)
	printf("element not found");
	
	
}
int min(int x,int y)
	{
		if(x<y)
		  return x;
		else
		  return y;
		
	}


