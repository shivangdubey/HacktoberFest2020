//Java program to sort an array consisting of 0s, 1s and 2s  without using any sorting algo.

import java.util.Arrays;
import java.util.Scanner;

public class array_012_sorting {


    public static void sort(int arr[]) {

        int length= arr.length;
        int temp[] = new int[length];
        int j=0;
        for(int i=0;i<length;i++) {
            if (arr[i] == 0)
                temp[j++]=arr[i];
        }
        for(int i=0;i<length;i++) {
            if (arr[i] == 1)
                temp[j++]=arr[i];
        }
        for(int i=0;i<length;i++) {
            if (arr[i] == 2)
                temp[j++] = arr[i];
        }   
            for (int i = 0; i < length; i++)
                arr[i] = temp[i];

    }


    public static void main(String args[]) {
        int a[] = {0, 1, 0, 2, 1, 2, 0, 2, 1, 0, 0, 1};
        System.out.println("The actual array: \n"+ Arrays.toString(a));
        sort(a);
        System.out.println("The sorted array: \n"+ Arrays.toString(a));

    }
}
