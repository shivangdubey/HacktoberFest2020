class Solution {
/*
*	Given a number n,print [1-n]
*	in Lexicographical order
*/

/*
*	Logic:
*	recurrsion
*/
    public List<Integer> res = new ArrayList<>();
    
    public List<Integer> lexicalOrder(int n) {
        for(int i = 1 ; i < 10 ; i++)
        populate(i,n);
        
        return res;
    }
    
    public void populate(int i,int n)
    {
        if(i > n)
            return ;
        
        res.add(i);
        
        for(int j = 0 ; j < 10 ; j++)
        {
            if(10*i+j > n)
                return ;
            
            populate(10*i+j,n);
        }
    }
}