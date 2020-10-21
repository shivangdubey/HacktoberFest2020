import java.util.*;
class substring{
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);
        String sent, rep, newstr;
        System.out.println("Enter a sentence: ");
        sent=sc.nextLine();
        System.out.println("Enter the string you want to replace: ");
        rep=sc.nextLine();
        System.out.println("Enter the string you want to see in you sentence: ");
        newstr=sc.nextLine();
        sent=sent.replace(rep,newstr);
        System.out.println("The new sentence is: "+sent);
    }
}