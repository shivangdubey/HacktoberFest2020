/*
PRIM'S ALGORITHM BY SAURABH VERMA
SAMPLE OUTPUT
-------------
Enter number of nodes : 5
Enter Matrix (NxN):
Enter distance between 1 and 0 5
Enter distance between 2 and 0 1
Enter distance between 2 and 1 6
Enter distance between 3 and 0 99
Enter distance between 3 and 1 4
Enter distance between 3 and 2 2
Enter distance between 4 and 0 99
Enter distance between 4 and 1 99
Enter distance between 4 and 2 4
Enter distance between 4 and 3 3
Enter initial vertex: 3
RESULT
(3, 2) = 2
(2, 0) = 1
(3, 4) = 3
(3, 1) = 4
*/

#include<stdio.h>
#define N 100
typedef struct myEdge
{
    int x;
    int y;
    int w;
    int used;
} edge;
typedef struct myEdgeList
{
    edge data[N];
    int num;
} edgeList;

int main()
{
    int n,i,j,v;
    edgeList eL,fL;
    eL.num=0;
    fL.num=0;

    printf("Enter number of nodes : ");
    scanf("%d",&n);

    int matrix[n][n];

    printf("Enter Matrix (NxN):\n");
    for(i=0;i<n;i++)
        for(j=0;j<=i;j++)
        {
            if(i==j)
                matrix[i][i]=0;
            else
            {
                printf("Enter distance between %d and %d ",i,j);
                scanf("%d",&matrix[i][j]);
                matrix[j][i]=matrix[i][j];
                eL.data[eL.num].x=i;
                eL.data[eL.num].y=j;
                eL.data[eL.num].w=matrix[i][j];
                eL.num++;
            }
        }

    int node[n];
    for(i=0;i<n;i++)
        node[i]=0;

    printf("\nEnter initial vertex: ");
    scanf("%d",&v);
    node[v]=1;
    
    int min=99;
    int parent=-1;
    int index = -1;

    while(fL.num!=n-1)
    {
        for(i=0;i<n;i++)
        {
            if(node[i]==1)
            {
                for(j=0;j<eL.num;j++)
                {
                    if((eL.data[j].x==i && node[eL.data[j].y]==0) || (eL.data[j].y==i && node[eL.data[j].x]==0))
                    {                      
                        if(eL.data[j].w<min)
                        {
                            min=eL.data[j].w;
                            if(eL.data[j].x==i)
                            {
                                parent = eL.data[j].x;
                                index = eL.data[j].y;
                            }
                            else
                            {
                                parent = eL.data[j].y;
                                index = eL.data[j].x;
                            }
                        }
                    }
                }
            }
        }
        node[index]=1;
        fL.data[fL.num].x=parent;
        fL.data[fL.num].y=index;
        fL.data[fL.num].w=min;
        fL.num++;
        parent=-1;
        index=-1;
        min=99;
    }
    printf("\nRESULT\n");
    for(i=0;i<fL.num;i++)
            printf("(%d, %d) = %d\n",fL.data[i].x,fL.data[i].y,fL.data[i].w);  
}