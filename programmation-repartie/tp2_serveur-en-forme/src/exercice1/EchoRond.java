package exercice1;

import java.net.*;
import java.io.*;

public class EchoRond {

    ServerSocket socketConnexion;
    Socket socketCommunication;
    ObjectInputStream objectInputStream;
    ObjectOutputStream objectOutputStream;

    public EchoRond(int port) throws IOException {
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
            processRequest1();
        } catch(IOException ignored){
        }
    }

    private void processRequest1() throws IOException {
        try {
            Rond rond = (Rond) objectInputStream.readObject();
            System.out.println(rond.toString());
            Rond cloneRond = rond.clone();
            objectOutputStream.writeObject(cloneRond);
        } catch (ClassNotFoundException ignored) {
        }
    }


//    public void requestLoop(){
//        int requestNumber;
//        boolean inProcess = true;
//
//        try{
//
//            while(inProcess){
//                requestNumber = objectInputStream.readInt();
//                if(requestNumber == 1){
//                    System.out.println("processRequest1()");
//                }
//                else if(requestNumber == 2){
//                    System.out.println("processRequest2()");
//                }
//                else if(requestNumber == 0){
//                    inProcess = false;
//                }
//            }
//        }catch(IOException ignored){
//        }
//    }
}
