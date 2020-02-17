import time
from pylab import *
import numpy as np
import matplotlib.pyplot as plt


def exponentiation_naive(nombre, puissance):
    resultat = nombre
    for n in range(1, int(puissance)):
        resultat = resultat * n
    return resultat


def exponentiation_rapide(nombre, puissance):
    if nombre == 1:
        return nombre
    valeur = exponentiation_naive(nombre, puissance / 2)
    if nombre % 2 == 0:
        return valeur * valeur
    else:
        return valeur * valeur * nombre


def tracer_courbes():
    # courbe 1
    abscisses = []
    ordonnees = []
    for puissance in range(4, 1000, 1):
        temps_debut = time.time()
        exponentiation_naive(10, puissance)
        temps_fin = time.time()
        abscisses.append(puissance)
        ordonnees.append((temps_fin - temps_debut) * pow(10, 6))
    x = np.array(abscisses)
    y = np.array(ordonnees)
    plt.plot(x, y, 'b', label="Exponentiation naive")

    # courbe 2
    abscisses = []
    ordonnees = []
    for puissance in range(4, 1000, 1):
        temps_debut = time.time()
        exponentiation_rapide(10, puissance)
        temps_fin = time.time()
        abscisses.append(puissance)
        ordonnees.append((temps_fin - temps_debut) * pow(10, 6))
    x = np.array(abscisses)
    y = np.array(ordonnees)
    plt.plot(x, y, 'r', label="Exponentiation rapide")

    plt.xlabel("Puissance de 10", fontdict=None, labelpad=None)
    plt.ylabel("Temps en nanosecondes", fontdict=None, labelpad=None)
    plt.legend(loc='upper left')
    plt.title("Exercice 3:exponentiation naive vs. rapide", fontdict=None, loc='center', pad=None)
    plt.show()


def main():
    tracer_courbes()


main()
