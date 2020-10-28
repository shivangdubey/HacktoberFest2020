// using merge sort to solve a AnnaCafe Problem
// Link - https://www.codechef.com/SNUC2020/problems/ANNACAFE
#include<bits/stdc++.h>
 #define ll  long long int
using namespace std;

// merge sort algorithm
void MergeSortedIntervals(vector<int>& v, int start, int mid, int end1) {


	vector<int> temp;

	int i, j;
	i = start;
	j = mid + 1;

	while (i <= mid && j <= end1) {

		if (v[i] <= v[j]) {
			temp.push_back(v[i]);
			++i;
		}
		else {
			temp.push_back(v[j]);
			++j;
		}

	}

	while (i <= mid) {
		temp.push_back(v[i]);
		++i;
	}

	while (j <= end1) {
		temp.push_back(v[j]);
		++j;
	}

	for (int i = start; i <= end1; ++i)
		v[i] = temp[i - start];

}


void MergeSort(vector<int>& v, int start, int end1) {
	if (start < end1) {
		int m = (start + end1) / 2;
		MergeSort(v, start, mid);
		MergeSort(v, mid + 1, end1);
		MergeSortedIntervals(v, start, mid, end1);
	}
}

//main body
int main(){
ll m,n,i,j,t;
int a;
cin >> t;

for(i=0;i<t;i++){
    cin >> n;
    vector<int>v;
        for(j=0;j<n;j++){
            cin>>a;
            v.push_back(a);
        }


    MergeSort(v, 0, n - 1);



    for(j=0;j<n;j=j+3){
            m=v[j];
            if(m!=v[j+1] || m!=v[j+2])
                 break;
        }
    cout << m<<endl;

}

return 0;
}
