// program to sort an array using Insertion Sort Algorithm.
#include <stdio.h>

#define MAXSIZE 10

void insertion_sort(int arr[], int n);

int main()
{
    int  i, arr[MAXSIZE], size;
    printf("\n Enter the number of elements in the array: ");
    scanf("%d", &size);
    printf("\n Enter the elements of the array: ");
    for(i=0; i<size; i++)
    {
        scanf("%d", &arr[i]);
    }
    insertion_sort(arr, size);

    return 0;

}



// function for Insertion Sort
void insertion_sort(int arr[], int size)
{
    int i, j, temp;
    for(i=1; i<size; i++)
    {
        temp = arr[i];
        j = i-1;
        while((temp < arr[j]) && (j >= 0))
        {
            arr[j+1] = arr[j];
            j = j-1;
        }
        arr[j+1] = temp;
    }
    printf("\n The Sorted Array is: \n");
    for(i=0; i<size; i++)
        printf("  %d\t", arr[i]);


}
