package exercice4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.Socket;
import java.util.Scanner;

class SommeClient {

    public static void main(String []args) {

        BufferedReader br;
        PrintStream ps = null;
        String line;
        Socket sock = null;
        int port;
        String message;

        Scanner scanner = new Scanner(System.in);
        
        port=12345;

        try {
            sock = new Socket("localhost",port);
        }
        catch(IOException e) {
            System.out.println("problème de connexion au serveur : "+e.getMessage());
            System.exit(1);
        }

        try {
            br = new BufferedReader(new InputStreamReader(sock.getInputStream()));

            while(true) {
                System.out.println("Saisir une serie de nombres entiers separes par des virgules: ");
                message = scanner.nextLine();

                if (message.equals("")) {
                    break;
                }
                
                ps = new PrintStream(sock.getOutputStream());
                ps.println(message);
                line = br.readLine();

                System.out.println("Resultat : "+line);
            }
            br.close();
            ps.close();
        }
        catch(IOException e) {
            System.out.println(e.getMessage());
        }
    }
}