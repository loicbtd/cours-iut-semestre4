import java.sql.Array;
import java.util.ArrayList;

public class Primality {
    public static void main(String[] args) {

        long launchTime;
        long finishTime;
        ArrayList<Integer> array = new ArrayList<>();

        launchTime = System.currentTimeMillis();

        for (int i = 0; i < Math.pow(10,5); i++) {
            if (check_primality_method1(i)) {
                array.add(i);
            }
        }

        finishTime = System.currentTimeMillis();

        System.out.println("Duration : " + (finishTime-launchTime));

        System.out.println("Resultat: ");
        for (Integer i:array) {
            System.out.print(i + ", ");
        }
    }

    public static boolean check_primality_method1(int n) {
        for (int i = 2; i < n; i++) {
            if (n%i == 0) {
                return false;
            }
        }
        return true;
    }

    public static boolean check_primality_method2() {
        return true;
    }
    public static boolean check_primality_method3() {
        return true;
    }
}
