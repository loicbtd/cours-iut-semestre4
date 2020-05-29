import math
import random
import sympy
import numpy
import numpy


def est_premier(entier):
    """
    :param entier: entier à tester
    :type entier: int
    :return: vrai si l'entier passé en paramètre est premier, faux sinon
    :rtype: bool
    """
    if entier == 1 or entier == 2:  # On traite déjà 1 et 2 qui sont premiers
        return True
    if entier % 2 == 0:  # Si le nombre est divisible par 2 ici, il n'est pas entier
        return False
    if entier ** 0.5 == int(entier ** 0.5):  # Si la racine carée de l'entier n'est pas entière, alors il n'est pas premier
        return False
    for diviseur in range(3, int(entier ** 0.5), 2):  # On teste tous les diviseurs entiers jusqu'à la racine carée de l'entier
        if entier % diviseur == 0:
            return False
    return True


def generer_nombre_premier_aleatoire():
    """
    :return: nombre premier aléatoire
    :rtype: int
    """
    p = numpy.random.choice(1000, 1)
    while est_premier(p) is False:
        p = numpy.random.choice(1000, 1)
    return int(p[0])


def trouver_racine_primitive(nombre_premier):
    """
    :param nombre_premier
    :type nombre_premier: int
    :return: racine primitive du nombre premier passé en paramètre
    :rtype: int
    """
    for i in range(1, nombre_premier):
        racines = []
        for k in range(1, nombre_premier):
            racines.append(i ** k % nombre_premier)
        if set(range(1, nombre_premier)).issubset(racines):
            return i
    return -1


def selectionner_a_dans_0_a_p_moins_2(p):
    """
    :param p: nombre premier p
    :return: choix d'un entier dans {0,...,p-2}
    :rtype: int
    """
    return random.choice(range(0, p - 1))


def generer_cles(p, g, a):
    """
    :param p: nombre premier
    :type p: int
    :param g: racine primitive
    :type g: int
    :param a: indicatrice d'Euler
    :type a: int
    :return: tuple clé publique, clé privée
    :rtype: tuple
    """
    A = g ** a % p
    cle_publique = (p, g, A)
    cle_privee = a
    return cle_publique, cle_privee


def chiffrer_message(message, cle_publique, b):
    """
    :param message: message à chiffrer
    :type message: int
    :param cle_publique:
    :type cle_publique tuple
    :param b: indicatrice d'Euler
    :type b: int
    :return: message chiffré
    :rtype: int
    """
    (p, g, A) = cle_publique
    B = g ** b % p
    c = message * A ** b % p
    return B, c


def dechiffrer_message(cryptogramme, cle_publique, cle_privee):
    """
    :param cryptogramme: message chiffré
    :type cryptogramme: int
    :param cle_publique:
    :type cle_publique: tuple
    :param cle_privee:
    :type cle_privee: tuple
    :return: message déchiffré
    :rtype: int
    """
    (p, g, A), a = cle_publique, cle_privee
    (B, c) = cryptogramme
    return B ** (p - 1 - a) * c % p


def main():
    p = generer_nombre_premier_aleatoire()
    g = trouver_racine_primitive(p)
    a = selectionner_a_dans_0_a_p_moins_2(p)

    (cle_publique, cle_prive) = generer_cles(p, g, a)
    b = selectionner_a_dans_0_a_p_moins_2(p)

    cryptogramme = chiffrer_message(62, cle_publique, b)
    print(dechiffrer_message(cryptogramme, cle_publique, cle_prive))


main()
