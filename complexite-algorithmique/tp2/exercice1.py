import time
from pylab import *
import numpy as np
import matplotlib.pyplot as plt


def recherche_lineaire(element_recherche, tableau):
    for element in tableau:
        if element == element_recherche:
            return element


def recherche_binaire(element_recherche, tableau):
    a = 0
    b = len(tableau) - 1
    m = (a + b) // 2
    while a < b:
        if tableau[m] == element_recherche:
            return m
        elif tableau[m] > element_recherche:
            b = m - 1
        else:
            a = m + 1
        m = (a + b) // 2
    return a


def tracer_courbes():

    # courbe 1
    abscisses = []
    ordonnees = []
    for puissance in range(4, 9, 1):
        taille_tableau = pow(10, puissance)
        tableau = [0]*taille_tableau
        temps_debut = time.time()
        recherche_binaire(1, tableau)
        temps_fin = time.time()
        abscisses.append(puissance)
        ordonnees.append((temps_fin - temps_debut)*pow(10, 6))
    x = np.array(abscisses)
    y = np.array(ordonnees)
    plt.plot(x, y, 'b', label="Recherche binaire")

    # courbe 2
    abscisses = []
    ordonnees = []
    for puissance in range(4, 9, 1):
        taille_tableau = pow(10, puissance)
        tableau = [0]*taille_tableau
        temps_debut = time.time()
        recherche_lineaire(1, tableau)
        temps_fin = time.time()
        abscisses.append(puissance)
        ordonnees.append((temps_fin - temps_debut)*pow(10, 6))
    x = np.array(abscisses)
    y = np.array(ordonnees)
    plt.plot(x, y, 'r', label="Recherche lineaire")

    plt.xlabel("Taille du tableau en puissance de 10", fontdict=None, labelpad=None)
    plt.ylabel("Temps en nanosecondes", fontdict=None, labelpad=None)
    plt.legend(loc='upper left')
    plt.title("Exercice 1: recherche lineaire vs. recherche binaire", fontdict=None, loc='center', pad=None)
    plt.show()


def main():
    tracer_courbes()


main()
