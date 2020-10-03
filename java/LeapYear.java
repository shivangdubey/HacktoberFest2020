package practice;

import java.util.Scanner;

public class LeapYear {
	
	public static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		
		System.out.println("Enter a year: ");
		
		int year = sc.nextInt();
		
		isLeapYear(year);
	}

	private static void isLeapYear(int year) {
		if(year % 4 == 0) System.out.println(year +" is leap year.");
		else System.out.println(year + " is not a leap year.");
	}

}
