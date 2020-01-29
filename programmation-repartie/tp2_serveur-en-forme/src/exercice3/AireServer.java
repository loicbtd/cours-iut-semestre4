package exercice3;

import exercice1.Rond;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

public class AireServer {
    ServerSocket socketConnexion;
    Socket socketCommunication;
    ObjectInputStream objectInputStream;
    ObjectOutputStream objectOutputStream;

    public AireServer(int port) throws IOException {
        socketConnexion = new ServerSocket(port);
    }


    public void mainLoop() throws IOException {
        while(true){
            socketCommunication = socketConnexion.accept();
            objectInputStream = new ObjectInputStream(socketCommunication.getInputStream());
            objectOutputStream = new ObjectOutputStream(socketCommunication.getOutputStream());
            objectOutputStream.flush();
            requestLoop();
        }
    }

    public void requestLoop(){


        try {
            int nombre_de_formes = objectInputStream.readInt();

            for (int i = 0; i < nombre_de_formes; i++) {
                int requestNumber = objectInputStream.readInt();
                switch(requestNumber) {
                    case 1:
                        processRequest1();
                        break;
                    case 2:
                        processRequest2();
                        break;
                }
            }
        } catch(IOException ignored){
        }
    }



    private void processRequest1() throws IOException {
        try {
            Rond rond = (Rond) objectInputStream.readObject();
            double aire = rond.aire();
            double perimetre = rond.perimetre();
            List<Double> caracteristiquesRond = new ArrayList<>();
            caracteristiquesRond.add(aire);
            caracteristiquesRond.add(perimetre);
            objectOutputStream.writeObject(caracteristiquesRond);
        } catch (ClassNotFoundException ignored) {
        }
    }

    private void processRequest2() throws IOException {
        try {
            Rectangle rectangle = (Rectangle) objectInputStream.readObject();
            double aire = rectangle.aire();
            double perimetre = rectangle.perimetre();
            List<Double> caracteristiquesRectangle = new ArrayList<>();
            caracteristiquesRectangle.add(aire);
            caracteristiquesRectangle.add(perimetre);
            objectOutputStream.writeObject(caracteristiquesRectangle);
        } catch (ClassNotFoundException ignored) {
        }
    }
}
