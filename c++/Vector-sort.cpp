// Input Format

// The first line of the input contains  where  is the number of integers. The next line contains  integers.
// Constraints

// , where  is the  integer in the vector.

// Output Format

// Print the integers in the sorted order one by one in a single line followed by a space.

// Sample Input

// 5
// 1 6 10 8 4
// Sample Output

// 1 4 6 8 10

// Solution

#include <vector>
#include <iostream>
#include<list>
using namespace std;
int main() {
    int i,j;
    cin>>i;
    int arr[i];
    for(j=0;j<i;++j)
    cin>>arr[j];
    list <int> v1{};
    for (j=0;j<i;++j)
    v1.push_back(arr[j]);
    v1.sort();
    list<int> ::iterator p=v1.begin();
    while (p!=v1.end())
    {
        cout<<*p<<" ";
        p++;
    }
    return 0;
}
