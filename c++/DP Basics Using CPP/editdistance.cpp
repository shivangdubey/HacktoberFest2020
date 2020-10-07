#include<iostream>
using namespace std;
int editdist(string str1,string str2, int len1,int len2)
{
    int dp[len1+1][len2+1];
    for (int i = 0; i <= len1; i++)
    {
        for (int j = 0; j <= len2; j++)
        {
            if (i == 0 && j == 0)
            {
                dp[i][j] = 0;
            }
            
            if(i == 0)
            {
                dp[i][j] =  j;
            }
            else if(j == 0)
            {
                dp[i][j] =  i;
            }
            else if(str1[i-1] == str2[j-1])
            {
                dp[i][j] = dp[i-1][j-1];
            }
            else 
            {
                dp[i][j] = min(min(dp[i][j-1],dp[i-1][j]),dp[i-1][j-1]) + 1;
            }
        }
    }
    return dp[len1][len2];
}
int main()
{
    int t;
    cin>>t;
    {
    string str1,str2;
    cin>>str1;
    cin>>str2;
    int len1 =  str1.length();
    int len2 =  str2.length();
    cout<<editdist(str1,str2,len1,len2);
    }
    return 0;
}