package practice;

import java.util.Scanner;

public class Palindrome {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Enter your text: ");
		String text = sc.nextLine();
		
		Check(text);
		
		sc.close();
	}
	
	static void Check(String text) {
		int length = text.length()-1;
		
		if(text.charAt(0) != text.charAt(length)) {
			System.out.println("String is not a palindrome");
		} else {
			System.out.println("String is a palindrome");
		}
	}
}
