#include <bits/stdc++.h>
using namespace std;

int BinarySearch(int sorted_array[], int left, int right, int element) 
{ 
    if (right >= left) 
    { 
        int middle = (left + right) / 2; 
        // If the element is at the middle itself 
        if (sorted_array[middle] == element) 
            return middle; 
        // If element < middle, then it can only be in left subarray 
        if (sorted_array[middle] > element) 
            return BinarySearch(sorted_array, left, middle - 1, element); 
        // Else the element can only be in right subarray 
        return BinarySearch(sorted_array, middle + 1, right, element); 
    } 
    // We reach here when element is not in array 
    return -1;  
} 

int main()
{
    int a[] = { 1, 5, 7, 3, 4, 8, 2, 9, 6 };
    int element = 5;
    int size = sizeof(a) / sizeof(a[0]); 
    sort(a, a + size);
    int result = BinarySearch(a, 0, size - 1, element); 
    if(result == -1)
        cout<<"Element is not in array";
    else
        cout<<"Element is at index "<< result;
    return 0;
}
