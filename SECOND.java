// minutes to year conversion.

import java.util.*;

public class SECOND {
    public static void main(String[] args) {
        System.out.println("Enter no. of minutes: ");
        Scanner sc = new Scanner(System.in);
        int min = sc.nextInt();

        MintoYear(min);
        sc.close();
    }

    public static void MintoYear(int min) {
        System.out.println("Input the number of minutes: "+min);
        int days = ((min/60)/24);
        int year = days/365;
        int remaining_days = days%365;
        System.out.println(min+" minutes is approximately "+year+" years and "+remaining_days+" days");
    }
}
