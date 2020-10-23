import java.util.InputMismatchException;
import java.util.Scanner;
import java.util.Random;
class Dice{
	private int nDice, sideDice;

	public Dice(){
		nDice = 0;
		sideDice = 0;
	}
	
	public static void main(String arg[]){
		Dice dice = new Dice();
		dice.readDice();
		
	} 

	public void readDice(){
		nDice = readKeyboard("Number of dices: ");
		sideDice = readKeyboard("Number of sides: ");
			roll(nDice, sideDice);
	}

	public int readKeyboard(String msg){
		int key = 0;
		boolean check = true;
		while(check){
			/*
			Read from keyboard and validate of the information is a number. 
			The loop will keep reading for the keyborad until the information is a valid integer number
			*/
			try{
				Scanner sc = new Scanner(System.in);
				System.out.print(msg);
				key = sc.nextInt();
				check = false;
			} catch (InputMismatchException e){
				System.out.println("Numbers only");
			}
		}
		
		return key;
	}

	public void roll(int d, int s){
		int valor = 0;
		// this loop will "roll" de number of d dices of s Sides
		for(int i = 0; i < d; i++){
		valor += (new Random().nextInt(s) + 1);
		}
		System.out.println("result:" + valor);
	}
}