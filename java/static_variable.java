/*Write java a program where we will access static variable from both instance and static method. Take a as instance variable and b as static variable. Implement two methods m1 as non static and m2 static that shows the values of a and b. Verify whether we can access non static variable in static method.*/
import java.util.Scanner;
public class Static
{
    int A;
    static int B;
    void M1()
    {
        Scanner C=new Scanner(System.in);
        System.out.println("Enter A: ");
        A=C.nextInt();
    }
    static void M2()
    {
        Scanner C=new Scanner(System.in);
        System.out.println("Enter B: ");
        B=C.nextInt();
    }
    public static void main(String args[])
    {
        Static S=new Static();
        S.M1();
        S.M2();
    }
}
