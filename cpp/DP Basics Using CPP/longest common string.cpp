#include<bits/stdc++.h>
using namespace std;

int main()
{
	string s1, s2;
	cin >> s1;
	cin >> s2;

	int dp[s1.length()+1][s2.length()+1] = {0};
	
	int maxlen = 0;
	
	int posr = 0, posc = 0;	
	
	for(int i = 0;i <= s1.length(); i++)
	{
		for(int j = 0;j <= s2.length(); j++)
		{
			if (i == 0 || j == 0) 
			{
				dp[i][j] == 0;
				continue;	
			}
			if(s1[i-1] == s2[j-1])
			{
				dp[i][j] = dp[i-1][j-1] + 1;
				
				if(maxlen < dp[i][j])
				{
					posr = i;
					posc = j;
					maxlen = dp[i][j];
				}
			}
			else
			{
				dp[i][j] = 0;
			}
		}
	}

}
