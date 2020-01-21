package exercice3;

import exercice1.Rond;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.util.Collection;
import java.util.List;
import java.util.Scanner;

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

            Scanner scanner = new Scanner(System.in);
            String caracteristiques;

            System.out.print("Saisir le nombre de formes a traiter: ");
            int nombreDeFormesATraiter = scanner.nextInt();
            for (int i = 0; i < nombreDeFormesATraiter; i++) {
                System.out.println("Saisir les caracteristiques de la forme.");
                System.out.println("> Pour un rond saisir le rayon sous la forme xx.xx");
                System.out.println("> Pour un rectangle saisir la largeur et la longueur sous la forme xx.xx,xx.xx");
                System.out.print("> Votre choix: ");
                caracteristiques = scanner.nextLine();
                System.out.println("\n\n\n\n\n\n");
            }
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
