#include <iostream>
using namespace std;

//fn to decide no of ways to paint fences, with k colors, such that no more than 2 adjacent fences have same color
int solve(int fences, int k){
    if(fences==0){
        return 1;
    }
    if(fences>2 && k<2){
        return 0;
    }
    long long diff = k;
    long long same = 0;
    long long total = diff + same;
    for(int i=2; i<=fences; i++){
        total = (total*(k-1)) + diff; 
        same = diff;
        diff = total-same;
    }
    return total;
}

int main() {
    int fences, colors;
    cin>>fences>>colors;
    cout<<solve(fences, colors);
    return 0;
}
