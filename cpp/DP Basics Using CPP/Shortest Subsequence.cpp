Shortest Subsequence
Send Feedback
Gary has two string S and V. Now Gary wants to know the length shortest subsequence in S such that it is not a subsequence in V.
Note: input data will be such so there will always be a solution.
Input Format :
Line 1 : String S of length N (1 <= N <= 1000)
Line 2 : String V of length M (1 <= M <= 1000)
Output Format :
Length of shortest subsequence in S such that it is not a subsequence in V
Sample Input :
babab
babba
Sample Output :
3




				PRACTICE

int solve(string S,string V)
{
	// Write your code here.
}
				SOLUTION



#define INF

#include<bits/stdc++.h>
using namespace std;
int solve(string S,string V){

int n = S.size(), m = V.size() ,i, j, prev;
 int dp[n+1][m+1] , next[n+1] [m+1];

for(i = 0; i<n; i++)
{ prev = -1;
for (j=0;j < m; j++)
{ if(S[i] == V[j])
 prev =j;
next[i+1][j+1] = prev;
}}

for(i = 1; i <= n; i++)
 dp[i][0] = 1;

for(i = 0; i <= m; i++){
    dp[0][i] = INF;
}
for(i=1; i<=n; i++)
{
    for(j=1; j<=m;j++)
    {
        if(next[i][j] == -1)
            dp[i][j] = 1;
            else{
            dp[i][j] = min(dp[i-1][j], 1+dp[i-1][next[i][j]]);
            }
    }
}
return dp[n][m];
}


int main()
{
	string S,V;
	cin>>S>>V;
	cout<<solve(S,V)<<endl;
	return 0;
}

