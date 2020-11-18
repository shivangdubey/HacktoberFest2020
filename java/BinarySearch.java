class BinarySearch { 
    int binarySearch(int a[], int left, int right, int x) 
    { 
        if (right >= left) { 
            int mid = left + (right - left) / 2; 
  
            if (a[mid] == x) 
                return mid; 
  
            if (a[mid] > x) 
                return binarySearch(a, left, mid - 1, x); 
  
            return binarySearch(a, mid + 1, right, x); 
        } 
        return -1; 
    } 
    public static void main(String args[]) 
    { 
        BinarySearch ob = new BinarySearch(); 
        int arr[] = { 56, 59, 66, 100}; 
        int n = arr.length; 
        int x = 66; 
        int result = ob.binarySearch(arr, 0, n - 1, x); 
        if (result == -1) 
            System.out.println("Element not present"); 
        else
            System.out.println("Element found at index " + result); 
    } 
} 
