#include<bits/stdc++.h>
using namespace std;

int subsetcount(vector<int> arr, int sum){
	int n = arr.size();
	int dp[n+1][sum+1];

	for(int i = 0; i <= n; i++)
	{
		dp[i][0] = 1;
	}
	
	for(int i = 1; i <= sum; i++)
	{
		dp[0][i] = 0;
	}
	
	for(int i = 1; i <= n; i++)
	{
		for(int j = 1; j <= sum; j++)
		{
			if(arr[i - 1] <= j)
			{
				dp[i][j] = dp[i-1][j] + dp[i-1][j - arr[i-1]];				
			}
			else
			{
				dp[i][j] = dp[i - 1][j];
			}
		}
	}
	return dp[n][sum];
}


int main()
{
    ios_base::sync_with_stdio(false);
    
 	cin.tie(NULL);
 	cout.tie(NULL);
 	
	int n = 6;
	
	int sum = 10;
	
	vector<int> arr = {2, 3 , 5, 6, 8, 10};
	
	cout << subsetcount(arr, sum);	
		
}
