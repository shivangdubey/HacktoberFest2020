
//1 232 34543 4567654 567898765 //

#include <iostream>
using namespace std;

int main() {
    int i,j,k;
     for(int i=1;i<=5;i++)
     {
         for(int j=i;j<=2*i-1;j++)
         {
             cout<<j;
         }
         for(int k=2*i-2;k>=i;k--)
         {
             cout<<k;
         }
         cout<<" ";
     }
	return 0;
}
