import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

public class AireThreadServer extends Thread {

    Socket socketCommunication;
    ObjectInputStream objectInputStream;
    ObjectOutputStream objectOutputStream;

    public AireThreadServer(Socket socketCommunication) {
        this.socketCommunication = socketCommunication;
    }

    public void run() {
        try {
            objectInputStream = new ObjectInputStream(socketCommunication.getInputStream());
            objectOutputStream = new ObjectOutputStream(socketCommunication.getOutputStream());
            objectOutputStream.flush();
            requestLoop();
        } catch (IOException ignored) {

        }
    }

    public void requestLoop(){
        try {
            processRequest();
        } catch(IOException ignored){
        }
    }

    private void processRequest() throws IOException {
        List<Object> formes = new ArrayList<>();
        try {
            while(true) {
                if(objectInputStream.readInt() != 0) break;
                formes.add(objectInputStream.readObject());
            }
        } catch (ClassNotFoundException ignored){
        }

        List<Double> caracteristiques;

        for (Object forme : formes) {
            caracteristiques = new ArrayList<>();
            if (forme instanceof Rond) {
                caracteristiques.add(((Rond) forme).aire());
                caracteristiques.add(((Rond) forme).perimetre());
            }
            else if (forme instanceof Rectangle) {
                caracteristiques.add( ((Rectangle) forme).aire());
                caracteristiques.add(((Rectangle) forme).perimetre());
            }
            objectOutputStream.writeObject(caracteristiques);
        }
    }
}
