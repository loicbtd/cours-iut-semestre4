import java.io.*;
import java.net.*;
import java.util.*;

class ServerThread extends Thread {

    Socket commReq;
    ObjectInputStream oisReq;
    ObjectOutputStream oosReq;
    int id;
    Game game;
    Player myPlayer; // l'objet player associé à ce thread
    Party currentParty; // l'objet party associé à player

    public ServerThread(int id, Socket commReq, Game game) {
        this.id = id;
        this.commReq = commReq;
        this.game = game;
        myPlayer = null;
        currentParty = null; // reste à null tant que le joueur n'a pas crée ou rejoint une partie
    }

    public void run() {

        try {
	    /* A COMPLETER :
	       - création des flux
	    */
            initLoop();
            requestLoop();
        } catch (Exception e) {
            System.out.println(id + " - client disconnected");
            if (myPlayer != null) game.removePlayer(myPlayer);
        }
    }

    public void initLoop() throws IOException, ClassNotFoundException {
	/* A COMPLETER :
	   faire une boucle qui s'arrête dès que le pseudo reçu n'existe pas déjà
	   dans la liste de game. Si c'est le cas, un nouveau joueur est créé et on
	   renvoie true au client, et sinon on renvoie false et on refait un tour de boucle.
	*/

    }

    public void requestLoop() throws IOException, ClassNotFoundException {

	/* A COMPLETER :
	   faire une boucle infinie qui recoit un identifiant de requête et 
	   en fonction de celui-ci, appeler la méthode associée pour traiter la requête
	   (cf ci-dessous pour les 3 méthodes possibles)
	*/
    }

    private void requestListPlayers() throws IOException, ClassNotFoundException {

	/* A COMPLETER :
	   - demander à game la liste des joueurs ayant créé une partie
	   - envoyer cette liste.
	*/
    }

    private void requestWaitPlayer() throws IOException, ClassNotFoundException {

	/* A COMPLETER :
	   - recevoir le nombre de tour (nbTurn) de la partie a créer
	   - création d'une nouvelle partie -> currentParty
	   - si currentParty == null : échec création donc renvoyer false puis return
	   - sinon, demander à currentParty d'attendre le début de la partie.
	   - envoyer le nom du deuxième joueur
	   - entamer la partie
	   - supprimer la partie de game
	*/
    }

    private void requestContestPlayer() throws IOException, ClassNotFoundException {
       
	/* A COMPLETER :
	   - recevoir booléen
	   - si booléen == true
	       - recevoir le pseudo du joueur contre lequel jouer
	       - demander a game si pseudo est dans une partie -> affecter currentParty
	       - si currentParty == null : échec pour rejoindre partie donc renvoyer false puis return
	   - sinon
	        - demander a game de choisir une partie aléatoirement -> affecter currentParty

	   - envoyer true
	   - envoyer le nom du joueur qui a créé la partie
	   - envoyer le nombre de tour
	   - mettre à jour le deuxième joueur de currentParty
	   - entamer la partie
	*/
	
 
    }

    private void partyLoop() throws IOException,ClassNotFoundException {

        for(int i=0;i<currentParty.nbTurn;i++) {

	    /* A COMPLETER :

	       - demander à currentParty le calcul à faire
	       - envoyer ce calcul
	       - recevoir la solution du joueur sous forme d'un entier
	       - intégrer la solution du joueur à currentParty
	       - si joueur est gagnant, envoyer true sinon false
	       - envoyer le nombre de points du joueur
	       - envoyer le nombdre de points de l'autre joueur
	    */

        }
    }
}
