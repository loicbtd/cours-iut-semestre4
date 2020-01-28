from itertools import combinations
import random
import time
from pylab import *
import numpy as np
import matplotlib.pyplot as plt


# def combinations(iterable, r):
#     # combinations('ABCD', 2) --> AB AC AD BC BD CD
#     # combinations(range(4), 3) --> 012 013 023 123
#     pool = tuple(iterable)
#     n = len(pool)
#     if r > n:
#         return
#     indices = range(r)
#     yield tuple(pool[i] for i in indices)
#     while True:
#         for i in reversed(range(r)):
#             if indices[i] != i + n - r:
#                 break
#         else:
#             return
#         indices[i] += 1
#         for j in range(i+1, r):
#             indices[j] = indices[j-1] + 1
#         yield tuple(pool[i] for i in indices)


def get_all_combinations(elements, value):
    all_combinations = []
    possible_combinations = []
    for i in range(0, len(elements)):
        all_combinations = all_combinations + list(combinations(elements, i))
    for combination in all_combinations:
        if sum(combination) == value:
            possible_combinations.append(combination)
    return sorted(possible_combinations, reverse=True)


def tracer_courbes():
    k = 6790
    abscisses = []
    ordonnees = []
    for nombre_valeurs in range(10, 24):
        c = [random.randint(0, 3000) for i in range(nombre_valeurs)]

        temps_debut = time.time()

        get_all_combinations(c, k)

        temps_fin = time.time()
        abscisses.append(nombre_valeurs)
        ordonnees.append((temps_fin - temps_debut) * pow(10, 3))
    x = np.array(abscisses)
    y = np.array(ordonnees)
    plt.plot(x, y, 'r', label="Durée (ms)")
    plt.xlabel("Nombre de valeurs", fontdict=None, labelpad=None)
    plt.ylabel("Durée de traitement en milisecondes", fontdict=None, labelpad=None)
    plt.legend(loc='upper left')
    plt.title("Exercice 1", fontdict=None, loc='center', pad=None)
    plt.show()


def main():
    # c =
    # k = 6790
    tracer_courbes()
    # print(get_all_combinations(c, k))

main()
