import math
import random
import sympy


def generer_nombre_premier_aleatoire():
    debut_plage_nombre = 100
    fin_plage_nombres = 100000
    nombres_premiers = [i for i in range(debut_plage_nombre, fin_plage_nombres) if sympy.isprime(i)]
    return random.choice([i for i in nombres_premiers])


def trouver_racine_primitive(nombre_premier):
    for i in range(1, nombre_premier):
        racines = []
        for k in range(1, nombre_premier):
            racines.append(i ** k % nombre_premier)
        if set(range(1, nombre_premier)).issubset(racines):
            return i
    return -1


def selectionner_a_dans_0_a_p_moins_2(p):
    return random.choice(range(0, p - 1))


def cles(p, g, a):
    A = g ** a % p
    publique = (p, g, A)
    prive = a
    return publique, prive


def chiffre(message, publique, b):
    (p, g, A) = publique
    B = g ** b % p
    c = message * A ** b % p
    return B, c


def dechiffre(cryptogramme, publique, prive):
    (p, g, A), a = publique, prive
    (B, c) = cryptogramme
    return B ** (p - 1 - a) * c % p

# def demarrer_outil_generation_cle():
#     import os
#     from sys import platform
#     if platform == "linux" or platform == "linux2":
#         clear = lambda: os.system('clear')
#     elif platform == "win32":
#         clear = lambda: os.system('cls')
#     else:
#         clear = lambda: print("clear not supported on your system")
#
#     choix_possibles = ['1', '2', '3']
#     print(
#         "### OUTIL EL GAMAL ###\n"
#         "1 : Générer une clé\n"
#         "1 : Générer une clé\n"
#         "2 : Chiffrer un message\n"
#         "3 : Déchiffrer un message\n"
#     )
#     choix = input()
#     while choix not in choix_possibles:
#         clear()
#         print("Erreur: Merci de saisir un choix parmis ceux proposer\n\n")
#         print(
#             "### OUTIL EL GAMAL ###\n"
#             "1 : Générer une clé\n"
#             "2 : Chiffrer un message\n"
#             "3 : Déchiffrer un message\n"
#         )
#         choix = input()



def main():
    p = generer_nombre_premier_aleatoire()
    g = trouver_racine_primitive(p)
    a = selectionner_a_dans_0_a_p_moins_2(p)

    (publique, prive) = cles(p, g, a)
    b = selectionner_a_dans_0_a_p_moins_2(p)

    cryptogramme = chiffre(98, publique, b)
    print(dechiffre(cryptogramme, publique, prive))


main()

# def generer_cle(p, g):
#     """ Génèrer la clé
#     :param p: nombre premier
#     :param g: racine primitive modulo p
#     :return: liste de 3 éléments contenant p, g et A=ga%p
#     """
#
#     # Choix de a dans {0,...,p-2}
#     print("Saisir un entier parmis:")
#     for i in range(0, p - 1, 1):
#         print(i, end=", ")
#     print("\n> ", end="")
#     a = input()
#
#     # Calcul de A = ga % p.

#     A = (g * a) % p
#
#     return [p, g, A]
#
#
# def chiffrement(cle, m):
#     """ Chiffrement
#     :param cle: liste de 3 elements: [p, g, A]
#     :param m: message à chiffrer
#     """
#     p = cle[0]
#     g = cle[1]
#     A = cle[2]
#
#     # Choix de b dans {0,...,p-2}
#     print("Saisir un entier parmis:")
#     for i in range(0, p - 1, 1):
#         print(i, end=", ")
#     print("\n> ", end="")
#     b = input()
#
#     # Calcul de B = gb % p
#     B = (g * b) % p
#
#     # Chiffrement du message
#     c = (A * b * m) % p
#
#     return [B, c, a]
#
#
# def dechiffrement(cle, message_chiffre):
#     """ Déchiffrement
#     :param cle: liste de 3 elements: [p, g, A]
#     :param message_chiffre: liste de 2 élèments: [B, c]
#     """
#
#     p = cle[0]
#     g = cle[1]
#     A = cle[2]
#     B = message_chiffre[0]
#     c = message_chiffre[1]
#
#     m = (B * p - 1 - a * c) % p
#
#     return m
#
#



# def trouver_racine_primitive(nombre_premier):
#     indicatrice_euler = trouver_indicatrice_euler(nombre_premier)
#     facteurs_premiers = trouver_facteurs_premiers(indicatrice_euler)
#     for facteur_premier in facteurs_premiers:
#         for i in range(1, facteur_premier + 1):
#             if facteur_premier * indicatrice_euler / nombre_premier * i % nombre_premier != 1:
#                 break
#             if i == facteur_premier:
#                 return facteur_premier
#     return 0


# def exponentiation_rapide(nombre, puissance):
#     if nombre == 0:
#         return 1
#     elif nombre % 2 == 0:
#         return exponentiation_rapide(nombre * nombre, puissance // 2)
#     else:
#         return nombre * exponentiation_rapide(nombre * nombre, puissance // 2)


# def trouver_indicatrice_euler(nombre):
#     return nombre - 1
#
#
# def trouver_facteurs_premiers(nombre):
#     if nombre == 1:
#         return set([])
#     else:
#         for k in range(2, nombre + 1):
#             if nombre % k == 0:
#                 L = trouver_facteurs_premiers(nombre / k)
#                 return L.union([k])