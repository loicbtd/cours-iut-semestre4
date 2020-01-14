package exercice3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.Socket;
import java.util.Scanner;

class EchoClient3 {

    public static void main(String []args) {

        BufferedReader br;
        PrintStream ps = null;
        String line;
        Socket sock = null;
        int port;
        String message;

        Scanner scanner = new Scanner(System.in);
        
        port=12346;

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
                message = scanner.nextLine();

                if (message.equals("")) {
                    break;
                }
                
                ps = new PrintStream(sock.getOutputStream());
                ps.println(message);
                line = br.readLine();

                System.out.println("le serveur me repond : "+line);
            }
            br.close();
            ps.close();
        }
        catch(IOException e) {
            System.out.println(e.getMessage());
        }
    }
}