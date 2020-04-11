import tools.Terminal;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;


public class Client {
    Socket communicationSocket;
    ObjectInputStream objectInputStream;
    ObjectOutputStream objectOutputStream;

    public Client(String host, int port) throws IOException {
        communicationSocket = new Socket(host, port);
    }

    public void mainLoop() throws IOException {
        while(true){
            objectInputStream = new ObjectInputStream(communicationSocket.getInputStream());
            objectOutputStream = new ObjectOutputStream(communicationSocket.getOutputStream());
            objectOutputStream.flush();
            requestLoop();
        }
    }

    public void requestLoop(){
        try {
            int requestId;
            boolean inProcess = true;

            while (inProcess) {

                requestId = Terminal.ask_integer("Enter the id of the request you want to process range=[1, 4] " +
                        "(other ids end the program)");

                switch (requestId) {
                    case 1:
                        processREQ1();
                        break;
                    case 2:
                        processREQ2();
                        break;
                    case 3:
                        processREQ3();
                        break;
                    case 4:
                        processREQ4();
                        break;
                    default:
                        objectOutputStream.writeInt(5);
                        inProcess = false;
                }
            }
        }catch(IOException ignored){
        }
    }

    private void processREQ1() throws IOException {
        objectOutputStream.writeInt(1);
        objectOutputStream.flush();

        int n = Terminal.ask_integer("Enter n");
        objectOutputStream.writeInt(n);
        objectOutputStream.flush();

        if (objectInputStream.readInt() == 0) {
            double result = objectInputStream.readDouble();
            System.out.println("Result: " + n + "+1.5 = " + result);
        }
        else {
            System.out.println("Error: n must be in included the following range: [0, 10]");
        }
    }

    private void processREQ2() throws IOException{
        objectOutputStream.writeInt(2);
        objectOutputStream.flush();

        // v1
        objectOutputStream.writeInt(Terminal.ask_integer("Enter v1"));
        objectOutputStream.flush();

        // v2
        objectOutputStream.writeInt(Terminal.ask_integer("Enter v2"));
        objectOutputStream.flush();

        // v3
        objectOutputStream.writeInt(Terminal.ask_integer("Enter v3"));
        objectOutputStream.flush();


        switch (objectInputStream.readInt()) {
            case 0:
                if (objectInputStream.readBoolean()) {
                    System.out.println("v2 + v3 > 50");
                }
                else {
                    System.out.println("v2 + v3 < 50");
                }
                break;
            case -1:
                System.out.println("Error on v1");
                break;
            case -2:
                System.out.println("Error on v2");
                break;
            case -3:
                System.out.println("Error on v3");
                break;
        }
    }

    private void processREQ3() throws IOException{
        objectOutputStream.writeInt(3);
        objectOutputStream.flush();

        objectOutputStream.writeObject("Hello");
        objectOutputStream.flush();

        objectOutputStream.writeObject(" World !");
        objectOutputStream.flush();

        if (objectInputStream.readInt() == -1) {
            return;
        }
        System.out.println("Length difference: " + objectInputStream.readInt());

        List<String> l = new ArrayList();
        l.add("element1");
        l.add("element2");
        objectOutputStream.writeObject(l);
        objectOutputStream.flush();

        if (objectInputStream.readInt() == -1) {
            return;
        }

        try {
            System.out.println("Result: " + (String) objectInputStream.readObject());
        } catch (ClassNotFoundException ignored) {
        }
    }

    private void processREQ4() throws IOException {
        objectOutputStream.writeInt(4);
        objectOutputStream.flush();

        objectOutputStream.writeInt(10);
        objectOutputStream.flush();

        if (objectInputStream.readInt() == -1) {
            return;
        }

        System.out.println("Saisir un nom de fichier: ");
        PrintWriter writer = new PrintWriter(new Scanner(System.in).nextLine(), "UTF-8");
        try {
            writer.println((String) objectInputStream.readObject());
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
        writer.close();
    }
}
