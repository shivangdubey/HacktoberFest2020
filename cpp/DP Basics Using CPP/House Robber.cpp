#include<bits/stdc++.h>
using namespace std;

int check(vector<int> arr, int pos, int sum, int size)
{
	if(pos > size)
		return 0;
		
	if(pos == size)
	{
		return arr[pos];
	}
	else
		return  max(check(arr, pos + 1, sum, size), arr[pos] + check(arr, pos+2, sum, size) );
	
}


void solve()
{
	int n;
	cin >> n;

	vector<int> arr(n);

	for(int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}
	
	cout << check(arr, 0, 0, arr.size()-1);
}

int main()
{
    ios_base::sync_with_stdio(false);
    
 	cin.tie(NULL);
 	cout.tie(NULL);
	solve();
		
}
