import java.io.IOException;

public class MainClient {
    public static void main(String[] args){
        try {
            AirClient client = new AirClient("localhost", 1235);
            client.mainLoop();
        } catch(IOException ignored){
        }
    }
}
