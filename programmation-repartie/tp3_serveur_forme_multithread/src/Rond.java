import java.io.Serializable;

public class Rond implements Serializable {

    private double rayon;

    public Rond(double rayon) {
        this.rayon = rayon;
    }

    public String toString() {
        String msg = "Rond,"+rayon;
        return msg;
    }

    public double getRayon() {
        return rayon;
    }

    public double perimetre() {
        return 3.14159*2.0*rayon;
    }

    public double aire() {
        return 3.14159*rayon*rayon;
    }

    public Rond clone() {
        return new Rond(rayon);
    }

    public boolean equals(Rond r) {
        if ( rayon == r.rayon) return true;
        return false;
    }
}
