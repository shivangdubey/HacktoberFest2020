#include<bits/stdc++.h>
using namespace std;

int recur(int t, string n, vector<int> &arr){
	
	if(t == n.size())
	{
		return arr[t] = 1;
	}
	
	if(n[t] == '0')
		return arr[t] = 0;
	
	if(arr[t] != -1)
		return arr[t];
		
	int res = 0;
	
	res += recur(t+1, n, arr);
	
	if(t < n.size()-1 && (n[t] == '1' || (n[t] == '2' && n[t+1]<='6')))
		res += recur(t+2, n, arr);
	
	return arr[t] = res;
}

void solve()
{
	string n;
	cin >> n;
	vector<int> arr(n.size()+1, -1);
	cout<<recur(0, n, arr);
//	vector<vector<int> > arr(n.size()+1, vector<int>(n.size()+1, 0));
	
	
}

int main()
{
    ios_base::sync_with_stdio(false);
 	cin.tie(NULL);
 	cout.tie(NULL);
	solve();
}
