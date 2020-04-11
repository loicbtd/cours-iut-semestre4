import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;


public class ServerThread extends Thread {

    Socket socketCommunication;
    ObjectInputStream objectInputStream;
    ObjectOutputStream objectOutputStream;

    public ServerThread(Socket socketCommunication) {
        this.socketCommunication = socketCommunication;
    }

    public void run() {
        try {
            objectOutputStream = new ObjectOutputStream(socketCommunication.getOutputStream());
            objectOutputStream.flush();
            objectInputStream = new ObjectInputStream(socketCommunication.getInputStream());
            requestLoop();
        } catch (IOException ignored) {
        }
    }

    public void requestLoop(){
        try {
            int requestId;
            boolean serving = true;

            while (serving) {
                requestId = objectInputStream.readInt();

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
                        serving = false;
                }
            }
        } catch(IOException ignored){
        }
    }

    private void processREQ1() throws IOException {
        final int[] range = {0, 10};

        int n = objectInputStream.readInt();

        if (n >= range[0] && n <= range[1]) {
            objectOutputStream.writeInt(0);
            objectOutputStream.flush();
            objectOutputStream.writeDouble(n+1.5);
            objectOutputStream.flush();
        }
        else {
            objectOutputStream.writeInt(-1);
            objectOutputStream.flush();
        }
    }


    private void processREQ2() throws IOException {
        final int[] rangeV1 = {0, 10};

        int v1 = objectInputStream.readInt();
        int v2 = objectInputStream.readInt();
        int v3 = objectInputStream.readInt();

        if (!(v1 >= rangeV1[0] && v1 <= rangeV1[1])) {
            objectOutputStream.writeInt(-1);
            objectOutputStream.flush();
            return;
        }

        if (!(v2 > v1)) {
            objectOutputStream.writeInt(-2);
            objectOutputStream.flush();
            return;
        }

        if (!(v3 > v2)) {
            objectOutputStream.writeInt(-3);
            objectOutputStream.flush();
            return;
        }

        objectOutputStream.writeInt(0);
        objectOutputStream.flush();

        objectOutputStream.writeBoolean(v2 + v3 > 50);
        objectOutputStream.flush();
    }

    private void processREQ3() throws IOException {
        String s1 = "";
        String s2 = "";
        try {
            s1 = (String) objectInputStream.readObject();
            s2 = (String) objectInputStream.readObject();
        } catch (Exception ignored) {
        }


        if (s1.length() < 1000 && s2.length() < 1000) {
            objectOutputStream.writeInt(0);
        }
        else {
            objectOutputStream.writeInt(-1);
        }
        objectOutputStream.flush();

        objectOutputStream.writeInt(s1.length() - s2.length());
        objectOutputStream.flush();

        List<String> l = new ArrayList<>();

        try {
            l = (List<String>) objectInputStream.readObject();
        } catch (ClassNotFoundException ignored) {
        }

        if (l.size() == 0) {
            objectOutputStream.writeInt(-1);
        }
        else {
            objectOutputStream.writeInt(0);
        }

        objectOutputStream.writeObject(s1 + s2);
        objectOutputStream.flush();
    }

    private void processREQ4() throws IOException {
        int n = objectInputStream.readInt();

        if (n > 0 && n < Math.pow(10, 9)) {
           objectOutputStream.writeInt(0);
        }
        else {
            objectOutputStream.writeInt(-1);
        }
        objectOutputStream.flush();

        objectOutputStream.writeObject("data");
        objectOutputStream.flush();
    }
}
