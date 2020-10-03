#include<bits/stdc++.h>
using namespace std;

int main()
{
	int n;
	vector<int> arr;
	cin >> n;
	while(n--)
	{
		int t;
		cin >> t;
		arr.push_back(t);
	}
	n = arr.size();

	int dp[n] = {0};

	dp[0] = 1;
	
	for(int i = 1; i < n; i++)
	{
		dp[i] = 1;
		for(int j = i -1; j >= 0; j--)
		{
			if(arr[j] > arr[i])
				continue;
			
			int temp = dp[j] + 1;
			if(dp[i] < temp)	
				dp[i] = temp;
		}
	}
	
	cout << *max_element(dp, dp+ n);
}
