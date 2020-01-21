package exercice1;

import java.net.*;
import java.io.*;

public class EnvoiRond {

    Socket communicationSocket;
    ObjectInputStream objectInputStream;
    ObjectOutputStream objectOutputStream;

    public EnvoiRond(String host, int port) throws IOException {
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
            processRequest1();
        }catch(IOException ignored){
        }
    }

    private void processRequest1() throws IOException {
        Rond rond = new Rond(20);
        objectOutputStream.writeObject(rond);

        try {
            Rond receivedRond = (Rond) objectInputStream.readObject();
            if (receivedRond.equals(rond)) {
                System.out.println("Ce sont les memes ronds");
            }
            else {
                System.out.println("Les ronds sont differents");
            }
        } catch (ClassNotFoundException ignored) {
        }
    }
}
