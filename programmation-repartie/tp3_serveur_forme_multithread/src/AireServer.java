import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

public class AireServer {

    ServerSocket socketConnexion;
    Socket socketCommunication;

    public AireServer(int port) throws IOException {
        socketConnexion = new ServerSocket(port);
    }

    public void mainLoop() throws IOException {
        while(true){
            socketCommunication = socketConnexion.accept();
            AireThreadServer aireThreadServer = new AireThreadServer(socketCommunication);
            aireThreadServer.start();
        }
    }
}
