def est_premier(nombre):
    try:
        assert nombre >= 2
    except AssertionError:
        return False
    for i in range(2, nombre):
        if nombre % i == 0:
            return False
    return True

def est_racine_primitive_modulo(p):
    



def generer_cle(p, g):
    """ Génèrer la clé
    :param p: nombre premier
    :param g: racine primitive modulo p
    :return: liste de 3 éléments contenant p, g et A=ga%p
    """

    # Choix de a dans {0,...,p-2}
    print("Saisir un entier parmis:")
    for i in range(0, p - 1, 1):
        print(i, end=", ")
    print("\n> ", end="")
    a = input()

    # Calcul de A = ga % p.
    A = (g * a) % p

    return [p, g, A]


def chiffrement(cle, m):
    """ Chiffrement
    :param cle: liste de 3 elements: [p, g, A]
    :param m: message à chiffrer
    """
    p = cle[0]
    g = cle[1]
    A = cle[2]

    # Choix de b dans {0,...,p-2}
    print("Saisir un entier parmis:")
    for i in range(0, p - 1, 1):
        print(i, end=", ")
    print("\n> ", end="")
    b = input()

    # Calcul de B = gb % p
    B = (g * b) % p

    # Chiffrement du message
    c = (A * b * m) % p

    return [B, c, a]


def dechiffrement(cle, message_chiffre):
    """ Déchiffrement
    :param cle: liste de 3 elements: [p, g, A]
    :param message_chiffre: liste de 2 élèments: [B, c]
    """

    p = cle[0]
    g = cle[1]
    A = cle[2]
    B = message_chiffre[0]
    c = message_chiffre[1]

    m = (B * p - 1 - a * c) % p

    return m


def demarrer_outil_generation_cle():
    import os
    from sys import platform
    if platform == "linux" or platform == "linux2":
        clear = lambda: os.system('clear')
    elif platform == "win32":
        clear = lambda: os.system('cls')
    else:
        clear = lambda: print("clear not supported on your system")

    choix_possibles = ['1', '2', '3']
    print(
        "### OUTIL EL GAMAL ###\n"
        "1 : Générer une clé\n"
        "2 : Chiffrer un message\n"
        "3 : Déchiffrer un message\n"
    )
    choix = input()
    while choix not in choix_possibles:
        clear()
        print("Erreur: Merci de saisir un choix parmis ceux proposer\n\n")
        print(
            "### OUTIL EL GAMAL ###\n"
            "1 : Générer une clé\n"
            "2 : Chiffrer un message\n"
            "3 : Déchiffrer un message\n"
        )
        choix = input()


def main():
    print(est_premier(2))
    # demarrer_outil_generation_cle()
    # cle = generer_cle(14, 3)
    #
    # print(dechiffrement(cle, chiffrement(cle, "bonjour")))
    # message = "Le code de Polybe"
    # encrypted_message = "3215133514151415413532541215"
    #
    #
    #
    # print(encrypt(carre, message))
    # print(decrypt(carre, encrypted_message))


main()
