#include<stdio.h>
#include<conio.h>


void main()
{
    int i,j,n;
    printf("How many even numbers you want : ");
    scanf("%d",&n);
    for(i=2;n>0;n--,i+=2)
{
    printf("  %d  ",i);
}
    getch();
}