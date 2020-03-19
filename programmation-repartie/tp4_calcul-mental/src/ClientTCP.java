import java.io.*;
import java.net.*;
import java.util.*;

class ClientTCP  {

    Socket commReq;
    ObjectInputStream oisReq;
    ObjectOutputStream oosReq;
    
    BufferedReader consoleIn; // flux de lecture lignes depuis clavier

    public ClientTCP(String serverIp, int serverPort) throws IOException {
	/* A COMPLETER :
	   - instanciation commReq pour se connecter au serveur
	   - instanciation des flux oosReq et oisReq
	*/	    

	consoleIn = new BufferedReader(new InputStreamReader(System.in));
    }

    public void initLoop() throws IOException,ClassNotFoundException {

	String line = null;
	boolean ok = false;

	while (!ok) {

	    /* A COMPLETER :
	    - saisir pseudo au clavier
	    - envoyer pseudo
	    - recevoir booléen dans ok
	    - éventuellement afficher msg en fonction de la valeur de ok
	    */	    
	}
    }

    public void requestLoop() throws IOException,ClassNotFoundException {

	String reqLine = null;
	String[] reqParts = null;
	boolean stop = false;
	int nbTurn = 0;
	String advName = "";

	while (!stop) {

	    System.out.print("Client> ");
	    reqLine = consoleIn.readLine();
	    reqParts = reqLine.split(" ");

	    if (reqParts[0].equals("players")) {

		/* NB : cette requête demande au serveur la liste des joueurs ayant
		   créé une partie
		*/
		
		/* A COMPLETER :
		   - envoyer identifiant requête (nb : aucun paramètres)
		   - recevoir liste joueursenvoyer pseudo
		   - afficher liste
		*/	    

	    }
	    else if (reqParts[0].equals("wait")) {

		/* NB : cette requête signal au serveur que le joueur se met en
		   attente d'un partenaire de jeu et que le serveur doit créer une nouvelle
		   partie avec X tours de jeu. Si le joueur a saisi correctement la requête
		   alors reqParts[1] contient cet entier nbTurn.
		   Si reqParts[1] n'existe pas ou bien ne correspond pas à un entier entre 1 et 10,
		   alors la requête est considérée comme malformée et un message d'erreur est affiché
		   Sinon, la requête est traitée.
		*/
		
		/* A COMPLETER :	    
		   - tests sur reqParts[1] et si ok, nbTurn = transfo de reqParts[1] en entier
		   - envoyer identifiant requête, puis nbTurn
		   - recevoir un booléen ok
		   - si ok == false : pas possible de créer la partie -> affichage message et continue;
		   - si ok == true : recevoir le nom de l'adversaire -> advName
		*/	    		
		System.out.println("Je joue contre "+advName+" en "+nbTurn+" coups");
		partyLoop(nbTurn);

	    }
	    else if (reqParts[0].equals("vs")) {

		/* NB : cette requête signale au serveur que le joueur veut entamer une partie
		   existante. Si reqParts[1] existe, alors il indique le nom du joueur qui a créé
		   la partie. Si reqParts[1] n'existe pas, le serveur doit choisir une partie 
		   au hasard.
		*/
		
		/* A COMPLETER :	    
		   - envoyer identifiant requête
		   - si reqParts[1] existe
		       - envoyer true
		       - envoyer reqParts[1]
		   - sinon
		       - envoyer false
		   - recevoir un booléen ok
		   - si ok == false : pas possible de rejoindre la partie -> affichage message et continue;
		   - si ok == true : 
		       - recevoir nom adversaire -> advName
		       - recevoir nombre de tours -> nbTurn
		*/	    		

		System.out.println("Je joue contre "+advName+ " en "+nbTurn+" coups");
		partyLoop(nbTurn);
	    }
	    else if (reqParts[0].equals("quit")) {
		stop = true;
	    }
	}
    }

    private void partyLoop(int nbTurn) throws IOException,ClassNotFoundException {

	String line = null;
	String solus = null;

	for(int i=0;i<nbTurn;i++) {

	    /* A COMPLETER :
	       - recevoir la String représentant l'opération à effecuter et l'afficher
	       - lire au clavier la réponse du joueur
	       - envoyer la réponse sous forme d'un int
	       - recevoir un booléen qui vaut true si le joueur a gagné, false sinon
	       - recevoir le nombre de points du joueur
	       - recevoir le nombre de points de l'autre joueur
	       - afficher si joueur a gagné et les points des deux joueurs	       
            */	    		
	}
    }
}
