
#include <bits/stdc++.h>
using namespace std;
//egg dropping problem
void eggdroppingpuzzle(int eggs,int floors)
{
    int **T=(int **)malloc(eggs*sizeof(int *));
    for(int i=0;i<eggs;i++)
        T[i]=(int *)malloc((floors+1)*sizeof(int));
    for(int i=0;i<eggs;i++)
        T[i][0]=0;
    for(int i=1;i<=floors;i++)
        T[0][i]=i;
    for(int i=1;i<eggs;i++)
    {
        for(int j=1;j<=floors;j++)
        {
            if((i+1)>j)
                T[i][j]=T[i-1][j];
            else
            {
                vector<int> v;
                for(int k=1;k<=j;k++)
                {
                    v.push_back(1+max(T[i-1][k-1],T[i][j-k]));
                }
                T[i][j]=*(min_element(v.begin(),v.end()));
            }
        }
    }
    printf("Minimum number of attempts to find which floor egg breaks from is %d\n",T[eggs-1][floors]);
    return ;
}
int main()
{
    int eggs,floors;
    printf("Enter number of floors and eggs\n");
    cin>>floors>>eggs;
    eggdroppingpuzzle(eggs,floors);
    return 0;

}
