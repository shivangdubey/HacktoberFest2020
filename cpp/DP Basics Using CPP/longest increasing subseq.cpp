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
//	8
//	10 9 2 5 3 7 101 18
	vector<int> ans;
	
	for(int i = 0; i < n; i++)
	{
		for(auto a:ans)
			cout << a<<" ";
			cout << endl;

		auto t = lower_bound(ans.begin(), ans.end(), arr[i]);			
		
		if(t == ans.end())
		{
			ans.push_back(arr[i]);
		}
		else
			*t = arr[i];
	}
	for(auto a: ans)
		cout << a << " ";
	
}
