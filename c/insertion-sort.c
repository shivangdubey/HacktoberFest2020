#include <stdio.h>

int i,j;

void insertionSort(int array[], int n) {
	
  int tmp;

  for (i = 1; i < n; i++) {
    tmp = array[i];
    j = i - 1;

    while ((j >= 0) && (array[j] > tmp)) {
      array[j + 1] = array[j];
        j--;
    }
    array[j + 1] = tmp;
   }
}

int main() {

  int array[] = {22,13,107,9,5,18};
  int n = sizeof(array)/sizeof(array[0]);
  
  insertionSort(array, n);
}
