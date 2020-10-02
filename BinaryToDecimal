import java.util.*;
public class BinaryToDecimal {
    public static int binaryToDecimal(int n) {
    int num = n;
    int dec_value = 0;
    int base = 1;

    int temp = num;
		while (temp > 0) {
        int last_digit = temp % 10;

        dec_value += last_digit * base;
        base = base * 2;
        temp/=10;
    }

		return dec_value;
}

    public static void main(String args[]) {
        Scanner s = new Scanner(System.in);

        int item = s.nextInt();
        System.out.println(binaryToDecimal( item));



    }

}


