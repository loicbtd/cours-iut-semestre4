import java.util.*;

class Party {

    private static Random loto = new Random(Calendar.getInstance().getTimeInMillis());
    Player player1;
    Player player2;
    int nbTurn;
    Player winner; // à chaque tour, contient l'objet player qui a gagné ou null si aucun n'a gagné
    private boolean start; // false par défaut et true dès que deux joueurs ont rejoint la partie  
    private int countGet; // nombre de demandes de la chaîne à calculer pour le tour courant
    private String calcul; // la chaîne à calculer pour le tour courant
    private int countRes; // le nombre de résultats reçus au tour courant
    private int goodResult; // le résultat du calcul pour le tour courant
    private int resultPlayer1; // le résultat envoyé par le joueur 1
    private int resultPlayer2; // le résultat envoyé par le joueur 2
    private int idFirst; // l'id (1 ou 2) du joueur qui a répondu en premier
    int ptsPlayer1; // le nombre de points du joueur 1
    int ptsPlayer2; // le nombre de points du joueur 2

    public Party(Player creator, int nbTurn) {
	player1 = creator;
	player2 = null;
	start = false;
	this.nbTurn = nbTurn;
    }

    public synchronized void setSecondPlayer(Player player2) {
	this.player2 = player2;
	// init attributs
	countGet = 0;
	countRes = 0;
	resultPlayer1 = 0;
	resultPlayer2 = 0;
	ptsPlayer1 = 0;
	ptsPlayer2 = 0;
        idFirst = 0;
        winner = null;
	/* A COMPLETER :
	   - start passe à true
	   - réveiller l'autre thread
	 */

    }

    public synchronized void waitforStart() {

	/* A COMPLETER :
	   - tant que start est faux :
	       - attendre (i.e. wait())
	 */
    }

    public synchronized String getCalcul() {
	
	/* A COMPLETER :
	   - si countGet == 0 : générer le calcul
	   - incrémenter countGet
	   - si countGet == 2, le remettre à 0

	 */
	return calcul;
    }

    public synchronized void integrateResult(int result, Player p) {

	/* A COMPLETER :
	   - si p est player1 : mettre à jour resultPlayer1 et éventuellement idFirst
	   - sinon si p est player2 : mettre à jour resultPlayer2 et éventuellement idFirst	       
	   - incrémenter countRes
	   - si countRes == 2 :
	       - trouver qui a gagné et mettre à jour winner, ptsPlayer1, ptsPlayer2 en fonction
	       - remettre idFirst à 0
	       - réveiller l'autre thread
	   - sinon
	       - tant que counRes != 2 :
	           - attentre (i.e. wait()
	       - remettre countRes à 0
	 */
    }



    private void generateCalcul() {
	
	int l = loto.nextInt(3);
	int nbOp = 2;
	int nbNum = 3;
	if (l == 1) {
	    nbOp = 3;
	    nbNum = 4;
	}
	else if (l == 2) {
	    nbOp = 4;
	    nbNum = 5;
	}
	ArrayList<String> lst = new ArrayList<String>();
	for(int i=0;i<nbNum;i++) {
	    int num = 1+loto.nextInt(10);
	    lst.add(String.valueOf(num));
	}
	for(int i=0;i<nbOp;i++) {
	    int op = loto.nextInt(3);
	    if (op == 0) lst.add("+");
	    else if (op == 1) lst.add("-");
	    else if (op == 2) lst.add("*");
	}
	for(int i=0;i<5;i++) {
	    int id = 2+loto.nextInt(nbOp+nbNum-3);
	    String s = lst.remove(id);
	    lst.add(nbOp+nbNum-2,s);
	}
	calcul = "";
	for(int i=0;i<nbNum+nbOp;i++) {
	    calcul = calcul + lst.get(i) + " ";
	}
	// calcule résultat
	ArrayDeque<Integer> lifo = new ArrayDeque<Integer>();
	for(int i=0;i<nbNum+nbOp;i++) {
	    String s = lst.get(i);
	    if (s.equals("+")) {
		int n2 = lifo.pop();
		int n1 = lifo.pop();
		lifo.push(n1+n2);
	    }
	    else if (s.equals("-")) {
		int n2 = lifo.pop();
		int n1 = lifo.pop();
		lifo.push(n1-n2);
	    }
	    else if (s.equals("*")) {
		int n2 = lifo.pop();
		int n1 = lifo.pop();
		lifo.push(n1*n2);
	    }
	    else {
		lifo.push(Integer.parseInt(s));
	    }
	}
	goodResult = lifo.pop();
    }
}
