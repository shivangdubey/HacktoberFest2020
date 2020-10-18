/* C++ program to implement the subset-sum problem
        using the Dynamic Programming*/

#include <bits/stdc++.h>
#include <ctime>
using namespace std;

/* Function to print the solution*/

void printsubset(int **temp,int *a,int i,int j)
{
    //printf("%d %d\n",i,j);
    if(j==0)
        return ;
    else if(i>0&&temp[i-1][j])
        printsubset(temp,a,i-1,j);
    else
    {

        printsubset(temp,a,i-1,j-a[i]);
        printf("%d\t",a[i]);
    }
}

/* Function to calculate the subset sum*/

void subsetsum(int *a,int n,int sum)
{
    int **temp=(int **)malloc(n*sizeof(int*));
    for(int i=0;i<n;i++)
        temp[i]=(int *)malloc((sum+1)*sizeof(int));
    for(int i=0;i<n;i++)
    {
        temp[i][0]=1;
    }
   /* for(int i=0;i<n;i++)
        printf("%d\n",a[i]);*/
    for(int i=0;i<n;i++)
    {
        for(int j=1;j<=sum;j++)
        {
            if(i==0)
                {if(a[i]==j)
                    temp[i][j]=1;
                else
                    temp[i][j]=0;}
            else if(a[i]<=j)
            {
                temp[i][j]=temp[i-1][j]+temp[i-1][j-a[i]];
                if(temp[i][j]>0)
                    temp[i][j]=1;
            }
            else
                temp[i][j]=temp[i-1][j];
        }
    }
    /*for(int i=0;i<n;i++)
    {
        for(int j=0;j<=sum;j++)
            printf("%d\t",temp[i][j]);
        printf("\n");
    }*/
    if(temp[n-1][sum])
     {
         printf("Subset exists\n");
         printsubset(temp,a,n-1,sum);
         printf("\n");
     }
     else
     {
         printf("Subset doesn't exist\n");
     }
}

/* Main Function */

int main()
{
    int a[]={2,3,7,8,10};
    sort(a,a+5);
    int sum;
    cin>>sum;
    subsetsum(a,5,sum);
    return 0;
}
