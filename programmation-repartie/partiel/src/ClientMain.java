import java.io.IOException;

public class ClientMain {
    public static void main(String[] args){
        try {
            Client client = new Client("localhost", 1236);
            client.mainLoop();
        } catch(IOException ignored){
        }
    }
}
