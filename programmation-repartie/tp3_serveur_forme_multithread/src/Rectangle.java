import java.io.Serializable;

public class Rectangle implements Serializable {

    private double longueur;
    private double largeur;

    public Rectangle(double largeur, double longueur) {
        this.largeur = largeur;
        this.longueur = longueur;
    }

    public String toString() {
        String msg = "Rectangle,"+largeur+","+longueur;
        return msg;
    }

    public double getLargeur() {
        return largeur;
    }

    public double getLongueur() {
        return longueur;
    }

    public double aire() {
        return largeur*longueur;
    }

    public double perimetre() {
        return 2.0*(largeur+longueur);
    }

    public Rectangle clone() {
        return new Rectangle(largeur,longueur);
    }

    public boolean equals(Rectangle r) {
        if ( ((largeur == r.largeur) && (longueur == r.longueur)) ||
                ((largeur == r.longueur) && (longueur == r.largeur)) ) return true;
        return false;
    }
}
