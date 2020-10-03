#include<bits/stdc++.h>
using namespace std;

int recur(int t, string n){
	
	if(t == n.size())
	{
		return 1;
	}
	
	if(n[t] == '0')
		return 0;
	
	int res = 0;
	
	res += recur(t+1, n);
	
	if(t < n.size()-1 && (n[t] == '1' || (n[t] == '2' && n[t+1]<='6')))
		res += recur(t+2, n);
	
	return res;
}

void solve()
{
	string n;
	cin >> n;
	cout<<recur(0, n);
}

int main()
{
    ios_base::sync_with_stdio(false);
 	cin.tie(NULL);
 	cout.tie(NULL);
	solve();
}
