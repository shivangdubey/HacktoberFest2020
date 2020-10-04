#include<bits/stdc++.h>
using namespace std;

int knapsack(int val[], int wt[], int w, int n){
		if(n == 0 || w == 0){
			return 0;
		}
		if(wt[n-1] <= w){
			return  max(val[n-1] + knapsack(val, wt, w - wt[n-1], n-1), knapsack(val, wt, w, n-1));	
		}
		else
		{
			return knapsack(val, wt, w, n - 1);
		}
}
		

int main()
{
    ios_base::sync_with_stdio(false);
    
 	cin.tie(NULL);
 	cout.tie(NULL);
 	
	int val[] = { 60, 100, 120 }; 
    int wt[] = { 10, 20, 30 }; 
    int w = 50;
	int n = 3;
	
	cout  << knapsack(val, wt, w, n);
		
}
