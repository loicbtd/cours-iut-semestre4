import java.util.*;

class Carte {
  
  private static Random loto = new Random(Calendar.getInstance().getTimeInMillis());

  private static int nbMe=0;
  private Map<Integer,Me> pop;
  private int sizeX;
  private int sizeY;

  public Carte(int sizeX, int sizeY) {
    this.sizeX = sizeX;
    this.sizeY = sizeY;
    pop = new HashMap<Integer,Me>();
  }

  public synchronized int createMe() {
    nbMe += 1;
    Me m = new Me(nbMe,loto.nextInt(sizeX),loto.nextInt(sizeY));
    pop.put(nbMe,m);
    return nbMe;
  }

  public synchronized boolean relativeMove(int idMe, int moveX, int moveY) {
    boolean ret = false;
    /*
      - prend dans pop Me dont l'id est idMe
      - récupère les coordonnées x,y du Me
      - si x+moveX sort de la carte retourne false
      - si y+moveY sort de la carte retourne false
      - sinon, déplace le Me en x+moveX,y+moveY
      - retourne true
    */
    return ret;
  }

  public synchronized int[] getMeCoords(int idMe) {
    int[] ret = null;
    /*
      - prend dans pop Me dont l'id est idMe
      - récupère les coordonnées x,y du Me
      - instancie un tableau tab de 2 entiers
      - tab[0] = x, tab[1] = y
      - retourne tab
    */
    return ret;
  }

  public synchronized Set<Me> getMeNeighbors(int idMe) {
    Set<Me> ret = null;
    /*
      - prend dans pop Me dont l'id est idMe
      - récupère les coordonnées x,y du Me
      - instancie un HashSet de Me
      - parcourt pop pour trouver les Me qui sont en x,y et les ajouter au set
      - retourne le HashSet
    */
    return ret;
  }
}
