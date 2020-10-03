#include<bits/stdc++.h>
using namespace std;

int lcs(string s, string t, int n, int m, vector< vector<int> >& arr)
{
	if(n == 0 || m == 0)
		return 0;
	
	if(arr[n-1][m-1] != 0)
	{
		return arr[n-1][m-1];
	}
	else{
	if(s[n-1] == t[m-1])
	{
		arr[n-1][m-1] = 1 + lcs(s, t, n-1, m-1, arr);
		return arr[n-1][m-1];
	}
	else
	{
		arr[n-1][m-1] = max(lcs(s, t, n, m - 1, arr), lcs(s, t, n - 1, m, arr));
		return arr[n-1][m-1];
	}
}
}

void solve()
{
	string s;
	string t;

	cin >> s;
	cin >> t;
	
	vector<vector<int> > arr(s.length(), vector<int>(t.length(), 0));
	cout << lcs(s, t, s.length(), t.length(), arr);		
}

int main()
{
    ios_base::sync_with_stdio(false);
    
 	cin.tie(NULL);
 	cout.tie(NULL);

	solve();
}
