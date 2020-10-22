#include<bits/stdc++.h>
using namespace std;
int main()
{
    int arr[100],n,i,j,t,k;
    cout<<"enter number of elements in the array\n";
    cin>>n;
    cout<<"enter elements \n";
    for(i=0;i<n;i++)
        cin>>arr[i];
    cout<<"bubble sort";
    for(k=0;k<n;k++){
    for(i=0;i<n;i++)
    {
        for(j=i;j<=i+1;j++)
        {
            if(arr[j]>arr[j+1])
            {
                
                t=arr[j+1];
                arr[j+1]=arr[j];
                arr[j]=t;

            }
        }
    }
    }
    cout<<"sorted array\n";
    for(i=0;i<n;i++)
    cout<<arr[i]<<" ";
}
