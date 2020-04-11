from math import sqrt


def est_premier(nombre):
    """ Tester si un nombre est premier
    :param nombre: nombre premier
    :return: True si le nombre est premier et False sinon
    """
    # si le nombre est inférieur à un, il ne peut pas être premier donc on retourne false
    if nombre <= 1:
        return False
    # si le nombre est 2 ou 3, on sait qu'il est premier donc on retourne true
    if nombre <= 3:
        return True
    # si le nombre est modulo 2 ou 3, on sait qu'il n'est pas premier puisqu'on a déjà exclu 2 et 3 précédement
    if nombre % 2 == 0 or nombre % 3 == 0:
        return False
    # on
    i = 5
    while i * i <= nombre:
        if nombre % i == 0 or nombre % (i + 2) == 0:
            return False
        i = i + 6
    return True


def puissance(x, y, p):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


def trouver_facteurs_premiers(s, phi):
    while phi % 2 == 0:
        s.add(2)
        phi = phi // 2

    for i in range(3, int(sqrt(phi)), 2):
        while phi % i == 0:
            s.add(i)
            phi = phi // i
    if phi > 2:
        s.add(phi)


def trouver_primitive(nombre_premier):
    
    s = set()
    if not est_premier(nombre_premier):
        return -1
    phi = nombre_premier - 1
    trouver_facteurs_premiers(s, phi)
    for r in range(2, phi + 1):
        flag = False
        for it in s:
            if puissance(r, phi // it, nombre_premier) == 1:
                flag = True
                break
        if not flag:
            return r
    return -1


def cles(p, g, a):
    A = g ** a % p
    publique = (p, g, A)
    prive  = a
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


def main():
    print(trouver_primitive(809))
    p = 23
    g = 5
    a = 20
    (publique, prive) = cles(p, g, a)
    b = 19
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
