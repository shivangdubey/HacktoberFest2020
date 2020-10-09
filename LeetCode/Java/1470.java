class Solution {
    public int[] shuffle(int[] nums, int n) {
        int res [] = new int[nums.length];
        int i = 0, j = n, k = 0;
        
        while ( i < n) {
            res[k] = nums[i];
            i++;
            k++;
            
            res[k] = nums[j];
            k++;
            j++;
        }
        return res;
    }
}