/*
    Topic- To find nth fibonacci number using Dynamic Programming
    Language- Java
    Code by- Jai Gaur
    Github profile & link- [Jai-Gaur-26](https://github.com/Jai-Gaur-26)
*/
import java.util.*;

public class fibonacci_using_dp {

    public static void main(String[] args) throws Exception {
        // write your code here
        Scanner scn = new Scanner(System.in);
        int n = scn.nextInt();
        int[] strg = new int[n+1]; //storage
        int ans = fiboM(n, strg); //M -> memoization
        System.out.println(ans);
        scn.close();
    }
    
    public static int fiboM(int n, int[] strg){
        if(n == 0 || n == 1){
            return n;
        }else if(strg[n] != 0){ //subproblem already solved
            return strg[n];
        }        
        
        int nm1 = fiboM(n-1, strg);
        int nm2 = fiboM(n-2, strg);
        int nthFib = nm1 + nm2;
        strg[n] = nthFib;
        return nthFib;
    }
    

}
