import java.util.*;

public class RotateAnArray 
{
	
	public static void rotate(int A[], int start, int end)
	{
		int j = end;
		for(int i=start ; i<j ; i++)
		{
			int temp = A[i];
			A[i] = A[j];
			A[j] = temp;
			
			j--;
		}
	}

	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		while(T != 0)
		{
			int n = sc.nextInt();
			int A[] = new int[n];
			
			for(int i=0 ; i<n ; i++)
			{
				A[i] = sc.nextInt(); 
			}

			int d = sc.nextInt();
			
			rotate(A, 0, d-1); //rotate part A
			rotate(A, d, n-1); //rotate part B
			rotate(A, 0, n-1); //rotate whole Array
			
			for(int i=0 ; i<n ; i++)
			{
				System.out.print(A[i]+" ");
			}
			System.out.println("");
			
			T--;
		}
		sc.close();
		
	
	}

}
