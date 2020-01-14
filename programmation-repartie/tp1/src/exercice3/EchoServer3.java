package exercice3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Scanner;

class EchoServer3 {

    public static void main(String []args) {


        BufferedReader br;
        PrintStream ps;
        String line;
        ServerSocket conn = null;
        Socket sock;
        int port;
        
        port = 12345;

        while(true) {
            try {
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

                while (true) {
                    line = br.readLine();
                    if (line == null) {
                        break;
                    }
                    System.out.println("le client me dit : " + line);
                    ps.println(line);
                }

                br.close();
                ps.close();
                port++;
            }
            catch(IOException e){
                System.out.println(e.getMessage());
            }
        }
    }
}