import random
import sympy
import numpy
import math


def convertir_chaine_vers_ascii(chaine):
    return int(''.join([f'{ord(c):03}' for c in chaine]))


def ascii_vers_chaine(valeur_ascii):
    valeur_ascii_chaine = str(valeur_ascii)
    if len(valeur_ascii_chaine) % 3 != 0:
        valeur_ascii_chaine = '0' + valeur_ascii_chaine
    return ''.join(chr(int(i)) for i in [valeur_ascii_chaine[i:i + 3] for i in range(0, len(valeur_ascii_chaine), 3)])


def generer_nombre_premier_aleatoire():
    debut_plage_nombre = 10 ** 4
    fin_plage_nombres = 10 ** 5
    nombres_premiers = [i for i in range(debut_plage_nombre, fin_plage_nombres) if sympy.isprime(i)]
    return random.choice([i for i in nombres_premiers])


def bezout(a, b):
    (r, u, v, R, U, V) = (a, 1, 0, b, 0, 1)

    while R != 0:
        q = r/R
        (r, u, v, R, U, V) = (R, U, V, r - q * R, u - q * U, v - q * V)
    return r, u, v


def clef(p1, p2):
    n = p1 * p2
    c = random.randint(10, 100000)
    (r, u, v) = bezout(c, (p1 - 1) * (p2 - 1))
    d = u
    return (n, c), d


def main():
    random.seed(1)
    p1 = generer_nombre_premier_aleatoire()
    p2 = generer_nombre_premier_aleatoire()


main()
