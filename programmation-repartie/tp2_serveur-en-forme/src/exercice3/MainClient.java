package exercice3;

import java.io.IOException;

public class MainClient {
    public static void main(String[] args){
        try {
            AirClient client = new AirClient("localhost", 1234);
            client.mainLoop();
        } catch(IOException ignored){
        }
    }
}
