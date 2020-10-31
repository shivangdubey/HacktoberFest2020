import java.util.*;
class day
{
   public static void main()
   {
       Scanner in=new Scanner(System.in);
       int d,m,y,i,n=0;
       System.out.println("Enter date(dd mm yyyy)");
       d=in.nextInt();
       m=in.nextInt();
       y=in.nextInt();
       int day[]={0,31,28,31,30,31,30,31,31,30,31,30,31};
       if(y%400==0||(y%100!=0&&y%4==0))
       {
           day[2]=29;
        }
       if(m>=1&&m<=12&&d>=1&&d<=day[m]&&y>0)
       {
           System.out.println("Valid Date");
           for(i=1;i<m;i++)
           {
               n=n+day[i];
            }
             System.out.println("Day Number="+(n+d));
        }
        else
        {
            System.out.println("Invalid Date");
        }
       
    }
}
