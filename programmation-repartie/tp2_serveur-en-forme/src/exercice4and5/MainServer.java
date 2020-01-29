package exercice4and5;

import java.io.IOException;

public class MainServer {
    public static void main(String[] args){
        try {
            AireServer server = new AireServer(1235);
            server.mainLoop();
        } catch(IOException ignored){
        }
    }
}
