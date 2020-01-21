package exercice1;

import java.io.IOException;

public class MainClient {
    public static void main(String[] args){
        try {
            EnvoiRond client = new EnvoiRond("localhost", 1234);
            client.mainLoop();
        } catch(IOException ignored){
        }
    }
}
