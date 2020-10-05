// Java program to print 
// hollow and solid rhombus patterns 
import java.io.*; 

class GFG 
{ 
	// Function for Solid Rhombus 
	static void solidRhombus(int rows) 
	{ 
		int i, j; 
		for (i=1; i<=rows; i++) 
		{ 
			// Print trailing spaces 
			for (j=1; j<=rows - i; j++) 
				System.out.print(" "); 
			
			// Print stars after spaces 
			for (j=1; j<=rows; j++) 
				System.out.print("*"); 
			
			// Move to the next line/row 
			System.out.println(); 
		} 
	} 

	// Function for Hollow Rhombus 
	static void hollowRhombus(int rows) 
	{ 
		int i, j; 
		for (i=1; i<=rows; i++) 
		{ 
			// Print trailing spaces 
			for (j=1; j<=rows - i; j++) 
				System.out.print(" "); 
			
			// Print stars after spaces 
			// Print stars for each solid rows 
			if (i==1 || i==rows) 
				for (j=1; j<=rows; j++) 
					System.out.print("*"); 
				
			// stars for hollow rows 
			else
				for (j=1; j<=rows; j++) 
					if (j==1 || j==rows) 
						System.out.print("*"); 
					else
						System.out.print(" "); 
			// Move to the next line/row 
			System.out.println(); 
		} 
	} 

	// utility program to print all patterns 
	static void printPattern(int rows) 
	{ 
		System.out.println("Solid Rhombus:"); 
		solidRhombus(rows); 
	
		System.out.println("Hollow Rhombus:"); 
		hollowRhombus(rows); 
	} 
	
	// driver program 
	public static void main (String[] args) 
	{ 
		int rows = 5; 
		printPattern (rows); 
	} 
} 

// Contributed by Pramod Kumar 
