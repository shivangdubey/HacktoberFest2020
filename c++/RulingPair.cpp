int RulingPair(vector<int> arr, int n) 
{
    // int a[100]; 
    vector<vector<int >> a(100);
    vector <int> maxl;
    for(int i=0;i<100;i++)
    {   
        a[i].push_back(0);
    }
    for(int i=0;i<n;i++)
    {
        string s = to_string(arr[i]);
        int m=s.length();
        int sum=0;
        for(int j=0;j<m;j++)
        {
            sum=sum + (int)s[j]-48;
        }
        a[sum].push_back(arr[i]);
    }
    for(int i=0;i<100;i++)
    {
        sort(a[i].begin(), a[i].end(), greater<int>());
        if(a[i].size()>2){
        a[i][0]=a[i][0]+a[i][1];
        maxl.push_back(a[i][0]);
        // cout<<a[i][0]<<endl;
        }
    }
    if(maxl.size()==0)
    {
        return -1;
    }
    sort(maxl.begin(), maxl.end(), greater<int>());
    // for(int i=0;i<maxl.size();i++)
    // {   
    //     cout<<maxl[i]<<endl;
    // }
    int ans=maxl[0];
    return ans;
    // code here
    
}