
/*
  You are given an array of integers nums, 
  there is a sliding window of size k which is moving from the very left of the array to the very right.
  You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.
*/
/* Data Structure Used : Stack*/

import java.util.*;
public class SlidindWindowMaximum2 {
	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);
		int n = scn.nextInt();
		int[] arr = new int[n];
		for(int i = 0; i < n; i++) {
			arr[i] = scn.nextInt();
		}
		int k = scn.nextInt();
		// logic of next greater element is very important to understand this problem
		
		Stack<Integer> st = new Stack<>();
		st.push(arr.length - 1);
		int[] nge = new int[arr.length];
		nge[arr.length - 1] = arr.length;
		for(int i = arr.length - 2; i >= 0; i--) {
			while(st.size() > 0 && arr[i] >= arr[st.peek()]) {
				st.pop();
			}
			if(st.size() == 0) {
				nge[i] = arr.length;
			}else {
				nge[i] = st.peek();
			}
			st.push(i);
		}
		int j = 0;
		for(int i = 0; i < arr.length - k; i++) {
			if(j < i) {
				j = i;
			}
			while(nge[j]  < i + k) {
				j = nge[j];
			}
			System.out.println(arr[j]);
		}
		
	}
}
