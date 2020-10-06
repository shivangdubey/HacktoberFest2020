import java.util.Scanner;

public class PrimeNumber {
	public static void main(String[] args) {
		new PrimeNumber().program();
	}

	public void program() {
		Scanner sc = new Scanner(System.in);
		int n;
		boolean isPrime = true;
		while (isPrime) {
			System.out.print("Enter number: ");
			n = sc.nextInt();

			isPrime = checkPrime(n);
			System.out.println(isPrime);
		}
	}

	public boolean checkPrime(int n) {
		if (n < 2) {
			return false;
		}

		for (int i = 2; i<n; i++) {
			if (n%i == 0) {
				return false;
			}
		}
		return true;
	}
}
