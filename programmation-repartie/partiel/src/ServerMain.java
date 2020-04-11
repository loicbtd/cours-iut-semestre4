import java.io.IOException;

public class ServerMain {
    public static void main(String[] args){
        try {
            Server server = new Server(1236);
            server.mainLoop();
        } catch(IOException ignored){
        }
    }
}