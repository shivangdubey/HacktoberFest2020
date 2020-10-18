/* C++ implementation of the weighted job scheduling problem
        using DP*/

#include <bits/stdc++.h>
using namespace std;


void JobScheduling(vector<tuple<int,int,int>> vti,int n)
{
    int *arr=(int *)malloc(n*sizeof(int));
    int *temp=(int *)malloc(n*sizeof(int));
    for(int i=0;i<n;i++)
    {
        arr[i]=get<2>(vti[i]);
        temp[i]=i;
    }
    for(int i=1;i<n;i++)
    {
        int j=0;
        while(j<i)
        {
            if(get<1>(vti[j])>get<0>(vti[i]))
                break;
                int prev=arr[i];
            arr[i]=max(arr[i],get<2>(vti[i])+arr[j]);
            if(arr[i]!=prev)
                temp[i]=j;
            j++;
        }
    }
    int maxv=0;
    for(int i=0;i<n;i++)
    {
        if(arr[i]>arr[maxv])
            maxv=i;
    }
    cout<<"Maximum profit-"<<arr[maxv]<<endl;
    int i=maxv;
    cout<<"Jobs-scheduled"<<endl;
    while(temp[i]!=i)
    {
        printf("%d %d\n",get<0>(vti[i]),get<1>(vti[i]));
        i=temp[i];
    }
    printf("%d %d\n",get<0>(vti[i]),get<1>(vti[i]));
    return;
}

/* Comparator function to help with the sort()*/

int comparator(const tuple<int,int,int> &a,const tuple<int,int,int> &b)
{
    return get<1>(a)<get<1>(b);
}

int main()
{
    vector<tuple<int,int,int>> vti;
    int n;
    cout<<"Enter number of jobs"<<endl;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cout<<"Enter start-time,end-time,profit"<<endl;
        int a,b,c;
        cin>>a>>b>>c;
        vti.push_back(tie(a,b,c));
    }
    sort(vti.begin(),vti.end(),comparator);
    JobScheduling(vti,n);

    return 0;

}
