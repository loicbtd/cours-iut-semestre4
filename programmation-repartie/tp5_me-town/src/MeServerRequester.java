import java.io.*;
import java.net.*;

class MeServerRequester extends Thread {

  private Socket commReq;
  private Socket commInfo;
  private Carte map;
  private int id;
  private ObjectInputStream ois; // used on commReq
  private ObjectOutputStream oos; // used on commReq
  private PrintStream ps; // used on commInfo

  public MeServerRequester(Socket commReq, Carte map) {
    this.commReq = commReq;
    this.map = map;
  }

  public void run() {
    try {
      /* create streams with MeClientRequester */
      ois = new ObjectInputStream(commReq.getInputStream());
      oos = new ObjectOutputStream(commReq.getOutputStream());
      oos.flush();

      /* NB : since the MeClientMessenger is created before creating above streams
	 we are nearly sure that the thread is ready to receive connection demands.
	 Nevertheless, there is the possibility that the JVM has not yet begun its
	 execution and in this case, a connection refused occurs.
      */
      
      /* connect to the MeClientMessenger thread : 
	 - ip = commReq.getInetAddress()
	 - port = 1+port used by the client socket commReq (NB : given by the OS),
	          thus 1+commReq.getPort();
      */
      commInfo = new Socket(commReq.getInetAddress(), commReq.getPort()+1);
      /* create streams with MeClientMessenger */
      ps = new PrintStream(commInfo.getOutputStream());


      /* à compléter :
	 - créer un Me,
	 - renvoyer l'id et la position du Me au client
      */

      /* à compléter :
	 - tant que vrai :
	    - recevoir l'id d'une requête
	    - appeler la méthode associée à la requête pour exécuter son protocole
      */

    }
    catch(IOException e) {
      System.out.println("Problème communication dans le thread "+id);
    }
  }

  public void requestMoveOf() {
  }

  public void requestNeighbors() {
  }
}
