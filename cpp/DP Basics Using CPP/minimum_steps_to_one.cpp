/* 
    MINIMUM STEPS TO ONE
    In this problem it is required a positive integer(input) to 1 in minimum number of steps
    The input value can be converted to 1 using following 3 steps:
    1. Subtract 1 from it. ( n = n - 1 ) 
    2. If its divisible by 2, divide by 2. ( if n % 2 == 0 , then n = n / 2  )
    3.If its divisible by 3, divide by 3. ( if n % 3 == 0 , then n = n / 3  )
*/
#include<iostream>
#include<climits>
using namespace std;
int bottomup(int n)
{
    int *dp = new int[n+1];
    dp[1]=0;
    for (int i = 2; i <=n; i++)
    {
        int op1=INT_MAX,op2=INT_MAX,op3=INT_MAX;
        op1=dp[i-1];
        if (i%2==0)
        {
            op2=dp[i/2];
        }
        if (i%3==0)
        {
            op3=dp[i/3];
        }
        dp[i]=min(op1,min(op2,op3))+1;
    }
    return dp[n];
}
int main()
{
    int n;
    cin>>n;
    int *dp = new int[n+1];
    for (int i = 0; i <=n ; i++)
    {
        dp[i]=-1;
    }
    cout<<bottomup(n);
}
