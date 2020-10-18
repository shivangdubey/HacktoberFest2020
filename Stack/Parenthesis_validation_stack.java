import java.util.*;
class Solution{
	
	public static void main(String []argh){

		Scanner sc = new Scanner(System.in);
		
		while (sc.hasNext()) {
			String input=sc.next();
      char[] ch=input.toCharArray();
      Stack<Character> st=new Stack<Character>();
      if(input.length()==0){
        System.out.println(false);
        continue;
      }
      for(int i=0;i<ch.length;i++){
        if(ch[i]=='{'||ch[i]=='('||ch[i]=='[')
          st.push(ch[i]);
        else{
          char c=ch[i];
          if(st.empty()==true){
            st.push(c);
            break;
          }
          else{
            if(c==st.pop()){continue;}
          }
        }  
      }
      if(st.empty()==true)
        System.out.println(true);
      else
        System.out.println(false);
		}
	}
}



