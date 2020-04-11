import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {

    ServerSocket socketConnexion;
    Socket socketCommunication;

    public Server(int port) throws IOException {
        socketConnexion = new ServerSocket(port);
    }

    public void mainLoop() throws IOException {
        while(true){
            socketCommunication = socketConnexion.accept();
            ServerThread serverThread = new ServerThread(socketCommunication);
            serverThread.start();
        }
    }
}
