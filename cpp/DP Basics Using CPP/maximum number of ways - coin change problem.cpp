#include<bits/stdc++.h>
using namespace std;


int noofcoin(int amt, int wt[], int n) 
{ 
	int k[n+1][amt+1];

	for(int i = 0; i <= n; i++){
		k[i][0]= 1;		
	}
	for(int i = 1; i <= amt; i++){
		k[0][i]= 0;		
	}
	
	for(int i = 1; i <= n; i++)
	{
		for(int j = 1; j <= amt; j++)
		{
			if(wt[i-1] <= j){
				k[i][j] = k[i-1][j] + k[i][j - wt[i-1]];			
			}	
			else
				k[i][j] = k[i-1][j];			
		}		
	}
	return k[n][amt];
	
} 

int main() 
{ 
	int coin[] = { 1, 2, 5}; 
	int amt = 5; 
	int n = sizeof(coin) / sizeof(coin[0]); 
	cout<< noofcoin(amt, coin, n); 
	return 0; 
} 

