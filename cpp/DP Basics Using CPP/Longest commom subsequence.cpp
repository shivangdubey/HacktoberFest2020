#include<bits/stdc++.h>
using namespace std;


void solve()
{
	string s;
	string t;

	cin >> s;
	cin >> t;
	
	vector<vector<int> > arr(s.length()+1, vector<int>(t.length()+1, 0));
	
	for(int i = 1; i <= s.length(); i++){
		for(int j = 1; j <= t.length(); j++)		
		{
			if(s[i-1] == t[j-1]){
				arr[i][j] = 1 + arr[i-1][j-1];
			}
			else
			{
				arr[i][j] = max(arr[i-1][j], arr[i][j-1]);
			}
			
		}
		
	}
	cout << arr[s.length()][t.length()];	
	
	
	
}

int main()
{
    ios_base::sync_with_stdio(false);
    
 	cin.tie(NULL);
 	cout.tie(NULL);

	solve();
	
		
}
