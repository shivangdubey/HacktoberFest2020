import java.util.Scanner;

public class AnyBaseToAnyBase {

	public static void main(String[] args) 
	{
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int bFrom = sc.nextInt();
		int bTo = sc.nextInt();
		int anyToDecimal = getValueInDecimal(n, bFrom);
		int decimalToAny = getValueInBase(anyToDecimal, bTo);
		System.out.println(decimalToAny);

	}
	
	public static int getValueInDecimal(int n, int bFrom) 
	{
		int ans = 0;
		int power = 0;
		
		while(n>0)
		{
			int rem = n % 10;
			n /= 10;
			
			ans += rem * Math.pow(bFrom, power);
			power++;
		}
		
		return ans;
	}
	
	public static int getValueInBase(int n, int bTo)
	{
		int place = 1;
		int ans = 0;
		while(n>0)
		{
			int rem = n % bTo;
			n /= bTo;
			
			ans += rem * place;
			place *= 10;
		}
		
		return ans;
	}

}
