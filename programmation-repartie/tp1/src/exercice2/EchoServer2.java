package tp1.exercice2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

class EchoServer2 {

    public static void main(String []args) {

        Scanner scanner = new Scanner(System.in);

        BufferedReader br = null;
        PrintStream ps = null;
        String line = null;
        ServerSocket conn = null;
        Socket sock = null;
        int port = -1;

        if (args.length != 1) {
            System.out.println("usage: Server port");
            System.exit(1);
        }


        do {
            try {
                port = Integer.parseInt(args[0]);
                conn = new ServerSocket(port);
            }
            catch(IOException e) {
                System.out.println("problème création socket serveur : "+e.getMessage());
                System.exit(1);
            }

            try {
                sock = conn.accept();
                br = new BufferedReader(new InputStreamReader(sock.getInputStream()));
                ps = new PrintStream(sock.getOutputStream());

                line = br.readLine();
                System.out.println("le client me dit : "+line);

                ps.println(line);
                br.close();
                ps.close();
            }
            catch(IOException e) {
                System.out.println(e.getMessage());
            }


        }while (true);
    }
}