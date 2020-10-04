#include<bits/stdc++.h>
using namespace std;

bool equalsum(vector<int> arr, int sum){
	
	int s = accumulate(arr.begin(), arr.end(), 0);
	
	if(s % 2 != 0)
	{
		return 0;
	}
	else
	{
		int n = arr.size();
		sum = sum/2;
		int t[n+1][sum+1];
		
		for(int i = 0; i <= n; i++)
			t[i][0] = 1;
			
		for(int i = 1; i <= sum; i++)
			t[0][i] = 0;
					
		for(int i = 1; i <= n; i++){
			for(int j = 1; j <= sum; j++){

				if(arr[i - 1] <= j){
					t[i][j] = t[i-1][j] || t[i-1][j - arr[i-1]];					
				}
				else
				{
					t[i][j] = t[i-1][j];
				}
			}	
		}
		return t[n][sum];		
	}
	
}



int main()
{
    ios_base::sync_with_stdio(false);
    
 	cin.tie(NULL);
 	cout.tie(NULL);
 	
	int n;
	cin >> n;
	
	int sum;
	cin >> sum;
	
	vector<int> arr;
	int t;
	
	for(int i = 0; i < n; i++)
	{
		cin >> t;
		arr.push_back(t);
	}
	
	cout << equalsum(arr, sum);	
		
}
