import java.io.*;
import java.net.*;
import java.util.*;

class MeClientRequester  {

  String ipServer;
  int portServer;
  String playerName;
  Socket commReq = null;
  ObjectInputStream ois = null;
  ObjectOutputStream oos = null;
  int idMe;
  int posX;
  int posY;

  public MeClientRequester(String playerName, String ipServer, int portServer) throws IOException {

    this.playerName = playerName;
    this.ipServer = ipServer;
    this.portServer = portServer;

    // connection to the server
    commReq = new Socket(ipServer, portServer);
    /* create the thread that manages info messages.*/
    MeClientMessenger t = new MeClientMessenger(commReq.getLocalPort()+1);
    t.start();

    // creating threads
    oos = new ObjectOutputStream(commReq.getOutputStream());
    oos.flush();
    ois = new ObjectInputStream(commReq.getInputStream());
  }

  public void handshake() throws IOException {
    
    // sending player name
    oos.writeObject(playerName);
    oos.flush();
    // receiving my identity, and position
    idMe = ois.readInt();
    posX = ois.readInt();
    posY = ois.readInt();
    System.out.println("My me is #"+idMe+" and is in ["+posX+","+posY+"]");
  }

  public void requestLoop() throws IOException {

    String reqLine = null;
    BufferedReader consoleIn = null;
    String[] reqParts = null;

    try {
      consoleIn = new BufferedReader(new InputStreamReader(System.in));
      System.out.print("MeClient> ");
      reqLine = consoleIn.readLine();
      reqParts = reqLine.split(" ");
      while (!reqParts[0].equals("QUIT")) {

	/* analyse de reqParts pour envoyer la requete au serveur
	   en appelant la bonne méthode */
	  
	System.out.print("MeClient> ");
	reqLine = consoleIn.readLine();
	reqParts = reqLine.split(" ");
      }
    }
    catch(IOException e) {
      System.out.println("communication problem: "+e.getMessage());
    }
  }

  public void requestMoveOf(int moveInX, int moveInY) {
  }

  public void requestNeighbors() {
  }
}
		
