class ArrayRotation {    
 public static void main(String[] args) {   
 
        //Making scanner class for user input
        Scanner sc = new Scanner(System.in);
        
        //Taking user input for n that determine the number of times an array should be rotated.    
        int n = sc.nextInt();  
        
          //Taking user input for d that is the size of the array.    
        int d = sc.nextInt();  
        
        //Taking array by user of size d
        int [] arr = new int [d];     
        for(int i = 0;i < d; i++) {
        arr[i] = sc.nextInt();
        }
          
            
        //Rotate the given array by n times    
        for(int i = 0; i < n; i++){    
            int j, temp;    
            //Stores the last element of array in temp   
            temp = arr[arr.length-1];    
            
            for(j = arr.length-1; j > 0; j--){    
                //Shifting element of the array by one position   
                arr[j] = arr[j-1];    
            }    
            //storing temp in last of array 
            arr[0] = temp;    
        }    
        
        System.out.println();    
            
        //Displays array after rotation      
        for(int e: arr){    
            System.out.print(e);    
        }    
    }    
}    
