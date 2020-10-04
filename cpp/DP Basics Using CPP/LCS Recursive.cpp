#include<bits/stdc++.h>
using namespace std;

int lcs(string s, string t, int n, int m)
{
	if(n == 0 || m == 0)
		return 0;
	
	if(s[n-1] == t[m-1])
	{
		return 1 + lcs(s, t, n-1, m-1);
	}
	else
	{
		return max(lcs(s, t, n, m - 1), lcs(s, t, n - 1, m));
	}
}


void solve()
{
	string s;
	string t;

	cin >> s;
	cin >> t;

	cout << lcs(s, t, s.length(), t.length());		
}

int main()
{
    ios_base::sync_with_stdio(false);
    
 	cin.tie(NULL);
 	cout.tie(NULL);
	solve();
	
}
