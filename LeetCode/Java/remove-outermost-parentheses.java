class Solution {
   //given a string of valid parenthese,remove the outer most parenthese for every primitive substring

  /*
  *Logic:
  *use a stack to track the outermost parenthese
  *and remove them from the given string
  */

    public String removeOuterParentheses(String s) {
        
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();

	//to track the index of outermost parenthese
        HashSet<Integer> remove = new HashSet<>();
        
        for(int i = 0 ; i < s.length() ; i++)
        {
            char c = s.charAt(i);
            if(c == '(')
                stack.push(i);
            else
            {
                int top = stack.pop();

		//if the stack is empty,then we have reached the outermost parentheses and add them to the hashset
                if(stack.isEmpty())
                {
                    remove.add(top);
                    remove.add(i);
                }
            }
        }

	//if the current index is found in hashset,then its the index of outermost parenthese and remove them

        for(int i = 0 ; i < s.length() ; i++)
        {
            if(!remove.contains(i))
            {
                sb.append(s.charAt(i));
            }
        }
        return sb.toString();
    }
}
