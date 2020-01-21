package exercice2;

import com.sun.xml.internal.ws.policy.privateutil.PolicyUtils;
import exercice1.Rond;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.util.List;

public class AirClient {
    Socket communicationSocket;
    ObjectInputStream objectInputStream;
    ObjectOutputStream objectOutputStream;

    public AirClient(String host, int port) throws IOException {
        communicationSocket = new Socket(host, port);
    }


    public void mainLoop() throws IOException {
        while(true){
            objectOutputStream = new ObjectOutputStream(communicationSocket.getOutputStream());
            objectOutputStream.flush();
            objectInputStream = new ObjectInputStream(communicationSocket.getInputStream());
            requestLoop();
        }
    }

    public void requestLoop(){
        try {
            sendRond();
            sendRectangle();
            readCaracteristiques();
        }catch(IOException ignored){
        }
    }

    private void sendRond() throws IOException {
        Rond rond = new Rond(20);
        objectOutputStream.writeInt(1);
        objectOutputStream.writeObject(rond);
    }

    private void sendRectangle() throws IOException {
        Rectangle rectangle = new Rectangle(20, 20);
        objectOutputStream.writeInt(2);
        objectOutputStream.writeObject(rectangle);
    }

    private void readCaracteristiques() throws IOException{
        try {
            List<Double> caracteristiques = (List<Double>) objectInputStream.readObject();
            System.out.println("Aire: " + caracteristiques.get(0));
            System.out.println("Perimetre: " + caracteristiques.get(1));
        } catch (ClassNotFoundException ignored) {
        }
    }
}
