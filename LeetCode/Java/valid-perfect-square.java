/*
*Given a number n return true if the number is a perfect square
*else return false
*/

/*
*Logic:
*the power of each number in its primefactorization
*has to be even
*/

class Solution {
    public boolean isPerfectSquare(int n) {
        int count = 0;
        
	//check the power of 2 in n
        while(n%2==0)
        {
            count++;
            n = n >> 1;
        }
        
	//if the power of 2 is odd return false;
        if((count&1)==1)
            return false;
        
        count = 0;
        
	//check if the number is divisble by i for i in range(3,sqrt(n))
        for(int i = 3 ; i <= Math.sqrt(n) ; i+=2)
        {
            while(n%i == 0)
            {
                n/=i;
                count++;
            }
            //if it contains odd power of i ,return false
            if((count&1)==1)
                return false;
            
            count = 0;
        }


	//if the number is not 1, return false
        if(n!=1)
            return false;
        else
            return true;
    }
}
