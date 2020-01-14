package exercice4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
import java.net.ServerSocket;
import java.net.Socket;

class SommeServer {

    public static void main(String []args) {


        BufferedReader br;
        PrintStream ps;
        String line;
        ServerSocket conn = null;
        Socket sock;
        int port;
        StringBuilder stringBuilder;
        int somme;
        char c;
        
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

                    somme = 0;
                    stringBuilder = new StringBuilder();
                    for (int i = 0; i < line.length(); i++){
                        c = line.charAt(i);
                        if (c != ',') {
                            stringBuilder.append(c);
                            if (i == line.length() - 1) {
                                somme =  somme + Integer.parseInt(stringBuilder.toString());
                            }
                        }
                        else {
                            somme =  somme + Integer.parseInt(stringBuilder.toString());
                            stringBuilder = new StringBuilder();
                        }
                    }
                    ps.println(stringBuilder);
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