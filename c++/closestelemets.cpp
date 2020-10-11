#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int a,b,n1,n2,q;
        cin>>a>>b;
        q = a/b;
        n1 = b * q;
        if(b * a > 0)
        {
            n2 = b * (q + 1);
        }
        else
        {
            n2 = b * (q - 1);
        }
        if(abs(a-n1)<abs(a-n2))
        {
            cout<<n1<<endl;
        }
        else
        {
            cout<<n2<<endl;
        }
        
        

    }
    return 0;
}