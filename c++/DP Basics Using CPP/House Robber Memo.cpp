#include<bits/stdc++.h>
using namespace std;

int check(vector<int> arr, int pos, int sum, int l, vector<int>& mem)
{
	if(pos < l)
		return 0;
		
	if(pos == l)
	{
		return arr[pos];
	}
	if(mem[pos] != -1)
		return mem[pos];
	else
		mem[pos] = max(check(arr, pos - 1, sum, l, mem), arr[pos] + check(arr, pos-2, sum, l, mem) );
	
	return mem[pos];
	
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
	vector<int> mem(n, -1);
	cout << check(arr, arr.size()-1, 0, 0, mem);

}

int main()
{
    ios_base::sync_with_stdio(false);
 	cin.tie(NULL);
 	cout.tie(NULL);
	solve();
}
