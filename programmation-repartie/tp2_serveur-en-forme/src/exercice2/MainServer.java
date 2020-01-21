package exercice2;

import exercice1.EchoRond;

import java.io.IOException;

public class MainServer {
    public static void main(String[] args){
        try {
            AireServer server = new AireServer(1234);
            server.mainLoop();
        } catch(IOException ignored){
        }
    }
}
