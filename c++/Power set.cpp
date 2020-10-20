#include<iostream>
#include<cmath>
using namespace std;

int main()
{
    int n;
    int c[100] , k;
    cout<<"Enter the number of elements is the set: ";
    cin>>n;
    int a[n];
    cout<<"Enter the elements of set: ";
    for(int i = 0; i < n; i++)
    {
        cin>>a[i];
    }
    cout<<"The power set :"<<endl;
    cout<<"{}";

    int p = pow(2,n);
    for(int i = 0; i < p; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if(i & (1 << j))
            {
                a[i] = c[i];
                k++;
        }
    }
    }
    for(int i = 0; i < k ;i++)
    {
        cout<<c[k]<<endl;
    }
}
