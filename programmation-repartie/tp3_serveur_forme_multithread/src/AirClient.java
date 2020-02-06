import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.util.ArrayList;
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
            List<Object> formes = saisirFormes();
            sendFormes(formes);
            readCaracteristiques(formes.size());
        }catch(IOException ignored){
        }
    }

    private List<Object> saisirFormes() {
        List<Object> formes = new ArrayList<>();
        Scanner scanner;
        String caracteristiques;

        // afficher consigne
        System.out.print("Saisir le nombre de formes a traiter: ");

        // saisie nombre de formes
        scanner = new Scanner(System.in);
        int nombreDeFormesATraiter = scanner.nextInt();

        // saisie des caracteristiques des formes
        for (int i = 0; i < nombreDeFormesATraiter; i++) {
            // afficher consigne
            System.out.println("Saisir les caracteristiques de la forme.\n" +
                    "> Pour un rond saisir le rayon sous la forme xx.xx\n" +
                    "> Pour un rectangle saisir la largeur et la longueur sous la forme xx.xx,xx.xx\n\n" +
                    "> Votre choix:");

            // saisie caracteristiques
            scanner = new Scanner(System.in);
            caracteristiques = scanner.nextLine();

            // traitement des donnees rentrees
            String[] caracteristiques_splitees = caracteristiques.split(",");
            if (caracteristiques_splitees.length == 1) {
                Rond rond = new Rond(Double.parseDouble(caracteristiques_splitees[0]));
                formes.add(rond);
            }
            else if (caracteristiques_splitees.length == 2) {
                Rectangle rectangle = new Rectangle(Double.parseDouble(caracteristiques_splitees[0]), Double.parseDouble(caracteristiques_splitees[1]));
                formes.add(rectangle);
            }
            else {
                System.out.println("bad format");
                formes.add(new Rectangle(10, 10));
            }
            System.out.println("\n\n\n\n\n\n");
        }
        return formes;
    }

    private void sendFormes(List<Object> formes) throws IOException {
        for (Object forme : formes) {
            objectOutputStream.writeInt(0);
            objectOutputStream.flush();
            if (forme instanceof Rond) {
                objectOutputStream.writeObject((Rond) forme);
                objectOutputStream.flush();
            }
            else if (forme instanceof Rectangle) {
                objectOutputStream.writeObject((Rectangle) forme);
                objectOutputStream.flush();
            }
        }
        objectOutputStream.writeInt(1);
        objectOutputStream.flush();
    }

    private void readCaracteristiques(int nombre_formes) throws IOException{
        for (int i = 0; i < nombre_formes; i++) {
            try {
                List<Double> caracteristiques = (List<Double>) objectInputStream.readObject();
                System.out.println("Objet " + i + ":");
                System.out.println("Aire: " + caracteristiques.get(0));
                System.out.println("Perimetre: " + caracteristiques.get(1));
                System.out.println("\n");
            } catch (ClassNotFoundException ignored) {
            }
        }
    }
}
