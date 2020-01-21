import time
from pylab import *
import numpy as np
import matplotlib.pyplot as plt


def trier_tri_bulles(data):
    n = len(data)
    swapped_elements = True
    while swapped_elements:
        swapped_elements = False
        for j in range(0, n - 1):
            if data[j] > data[j + 1]:
                swapped_elements = True
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def insere(x, liste):
    if not liste:
        return [x]
    elif x <= liste[0]:
        return [x] + liste
    else:
        return [liste[0]] + insere(x, liste[1:len(liste)])


def fusion(liste1, liste2):
    if not liste1:
        return liste2
    elif not liste2:
        return liste1
    else:
        return fusion(liste1[1:len(liste1)], insere(liste1[0], liste2))


def trier_tri_fusion(liste):
    n = len(liste)

    if n == 0 or n == 1:
        return liste
    else:
        return fusion(trier_tri_fusion(liste[0:n // 2]), trier_tri_fusion(liste[n // 2:n]))


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
    for puissance in range(0, 5, 1):
        taille_tableau = pow(10, puissance)
        tableau = []
        for valeur in range(taille_tableau-1, 0, -1):
            tableau.append(valeur)
        temps_debut = time.time()
        # trier_tri_fusion(tableau)
        temps_fin = time.time()
        abscisses.append(puissance)
        ordonnees.append((temps_fin - temps_debut) * pow(10, 6))
    x = np.array(abscisses)
    y = np.array(ordonnees)
    plt.plot(x, y, 'b', label="Tri fusion")

    # courbe 2
    abscisses = []
    ordonnees = []
    for puissance in range(0, 5, 1):
        taille_tableau = pow(10, puissance)
        tableau = []
        for valeur in range(taille_tableau - 1, 0, -1):
            tableau.append(valeur)
        temps_debut = time.time()
        trier_tri_bulles(tableau)
        temps_fin = time.time()
        abscisses.append(puissance)
        ordonnees.append((temps_fin - temps_debut) * pow(10, 6))
    x = np.array(abscisses)
    y = np.array(ordonnees)
    plt.plot(x, y, 'r', label="Tri a bulles")

    plt.xlabel("Taille du tableau en puissance de 10", fontdict=None, labelpad=None)
    plt.ylabel("Temps en nanosecondes", fontdict=None, labelpad=None)
    plt.legend(loc='upper left')
    plt.title("Exercice 2: tri fusion vs. tri bulle", fontdict=None, loc='center', pad=None)
    plt.show()


def main():
    tracer_courbes()


main()
