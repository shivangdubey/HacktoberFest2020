//#include <conio.h>
#include <stdlib.h>
#include <stdio.h>

#define MAXELT 10001

void main()  //overhead - read the numbers, print the results.
{
  int i=-1,n=0,L[MAXELT],m,s;
  char t[10];
  void largest_and_second_largest(int a[],int n,int *m,int *s);

  do {
    if (i!=-1)
      L[i++]=n;
    else
      i++;
    printf("\nEnter a number>");
    gets(t);
    if (sscanf(t,"%d",&n)<1)
      break;
  } while (1);
  largest_and_second_largest(L,i,&m,&s);
  printf("\nThe maximum is %d and the second-largest is %d.",m,s);
}

//The action lies here
void largest_and_second_largest(int a[],int n,int *m,int *s)
{
  int *I,                       //stores the losers
      size,                     //stores the current level in the tree
      i,j,                      //indexed
      lu,                       //stores the last compared element in the
                                //current level
      max,                      //stores the largest number
      slarge,                   //stores the second largest number
      sindex;                   //stores the index of the second largest number
  void swap(int *a,int *b);

  size=1; lu=-1;                //initialize - level one and no number used
  I=(int *)malloc(sizeof(int)*n);
  for (i=0;i<n;i++)             //initialize - no loser yet
    I[i]=-1;
  for (;;) {                    //loop until size-1 becomes more than n
    i=size-1;
    if (i>=n)
      break;                    //loop exit
    j=size+i;
    if (j>=n && i!=n-1)         //if the last element of the array has
      j=n-1;                    //not been considered, use it
    if (j>=n)
      if (lu<0)
        break;                  //loop exit
      else {
        j=lu;                   //store the used number in lu
        lu=-1;
      }
    for (;;) {                  //another seemingly infinite loop
      if (a[i]>a[j])            //swap if out of order
        swap(&a[i],&a[j]);
      else
        I[i]=I[j];              //otherwise, just store in the loser list
      I[j]=i;
      i=j+size;                 //next number
      if (i>=n)
        break;                  //inner loop exit
      else {
        j=i+size;               //next
        if (j>=n && i!=n-1)     //if the last element of the array has
          j=n-1;                //not been considered, use it
        if (j>=n)
          if (lu>0) {
            j=lu;               //take in last used
            lu=-1;              //empty last used
          }
          else {
            lu=i;               //if there is no earlier last used, store the
                                //current number as last used
            break;
          }
      }
    }
    size=2*size;                //move to the next level
  }
  max=a[n-1];                   //largest is found
  sindex=I[n-1];                //find the second largest by simple comparison
  slarge=a[sindex];             //in the loser list for the maximum
  while (sindex!=-1) {
    sindex=I[sindex];
    if (sindex!=-1 && a[sindex]>slarge)
      slarge=a[sindex];
  }
  *m=max;
  *s=slarge;
  free(I);                      //free and return
}

void swap(int *a,int *b)        //swap two elements
{
  int temp;

  temp=*a;
  *a=*b;
  *b=temp;
}
