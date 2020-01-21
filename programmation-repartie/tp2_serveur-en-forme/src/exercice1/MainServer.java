package exercice1;

import java.io.IOException;

public class MainServer {
    public static void main(String[] args){
        try {
            EchoRond server = new EchoRond(1234);
            server.mainLoop();
        } catch(IOException ignored){
        }
    }
}
