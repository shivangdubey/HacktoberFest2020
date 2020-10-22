import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.io.PrintWriter;
class TestClass {
    public static void main(String args[] ) throws Exception {
        PrintWriter out=new PrintWriter(System.out);
        Myscanner s=new Myscanner();
        int n=s.nextInt();
        int m=31;
        long dp[][]=new long[n+1][m+1];
        for(int i=0;i<m+1;i++){
            dp[0][i]=0;
        }
		long arr[]=new long[n+1];
		for(int i=1;i<n+1;i++){
			arr[i]=s.nextLong();}
            for(int i=1;i<n+1;i++){
            long k=arr[i],temp=0,sum=0;
            for(int j=0;j<m+1;j++){
                if(k%2==0){
                    long p=(long)Math.pow(2,j);
                    sum=p-temp;
                }
                else{
                    temp+=(long)Math.pow(2,j);
                    sum=0;
                }
            dp[i][j]=dp[i-1][j]+sum;
            k=k/2;
            }
		}
		int query=s.nextInt();
		for(int i=0;i<query;i++){
			int l=s.nextInt();
			int r=s.nextInt();
            long min=Integer.MAX_VALUE;
            for(int j=0;j<m+1;j++){
                min=Math.min(dp[r][j]-dp[l-1][j],min);
            }   
          out.println(min);
          out.flush();
        
    }
	}
		
static int minimumAdd(int l,int r,long[] arr){
	int count=0;
	long min=arr[l];
	int i=0;
    boolean flag=true;
	for(i=l+1;i<r;i++){
		if((min&arr[i])==0){
            flag=false;
			break;
		}
        min=min&arr[i];
	}
	if(flag){
		return 0;
	}
	for(int j=l;j<r;j++){
		if((arr[j]&(long)1)==0){
			count++;
		}
	}
	return count;
}

    static class Myscanner{
        private BufferedReader br;
        private StringTokenizer tr;
        public Myscanner()
        {
            br=new BufferedReader(new InputStreamReader(System.in));
        }
        public String next(){
            try{
                while(tr==null||!tr.hasMoreTokens())
                {
                    tr=new StringTokenizer(br.readLine());
                }
            }
            catch(Exception e)
            {
                e.printStackTrace();
            }
            return tr.nextToken();
        }
        public int nextInt()
        {
            return Integer.parseInt(next());
        }
        public long nextLong()
        {
            return Long.parseLong(next());
        }
    }

    }

