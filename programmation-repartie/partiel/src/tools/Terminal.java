package tools;

import java.util.InputMismatchException;
import java.util.Scanner;

public final class Terminal {

    private Terminal() {
        throw new UnsupportedOperationException();
    }

    public static int ask_integer(String message) {
        Scanner scanner = new Scanner(System.in);
        System.out.print(message + ": ");
        return scanner.nextInt();
    }
}
