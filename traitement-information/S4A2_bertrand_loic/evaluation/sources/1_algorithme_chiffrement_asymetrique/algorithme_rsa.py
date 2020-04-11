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


def trouver_pgcde_avec_bezout(entier_a, entier_b):
    """
    :param entier_a
    :type entier_a: int
    :param entier_b
    :type entier_b: int
    :return tuple (r, u, v) où r = PGCD(entier_a, entier_b) et u, v deux entiers tels que a*u + b*v = r
    """
    r1, u1, v1 = entier_a, 1, 0  # On instancie r, u et v
    r2, u2, v2 = entier_b, 0, 1  # On instancie r, u et v
    while r2 != 0:
        q = r1 // r2
        rs, us, vs = r1, u1, v1
        r1, u1, v = r2, u2, v2
        rp, up, vp = (rs - q * r2), (us - q * u2), (vs - q * v2)
    return r1, u1, v1


def generer_cle():
    """
    :return: un tuple contenant deux tuples qui sont respectivement la clé privée et la clé publique
    :rtype: tuple
    """
    # Génération aléatoire de deux nombres premiers p1 et p2
    p1 = numpy.random.choice(1000, 1)
    p2 = numpy.random.choice(1000, 1)
    while est_premier(p1) is False:
        p1 = numpy.random.choice(1000, 1)
    while est_premier(p2) is False:
        p2 = numpy.random.choice(1000, 1)
    # Calcul de n
    n = p1 * p2
    # Calcul de m
    m = (p1 - 1) * (p2 - 1)
    # Recherche de c tel que pgcd(m,c)=1 ) et de d = pgcde(m,c) tel que 2 < d < m
    r = 10
    d = 0
    c = 0
    while r != 1 or d <= 2 or d >= m:  # Tant que r≠1, on réitère
        c = numpy.random.choice(1000, 1)  # On tire c aléatoirement
        r, d, v = trouver_pgcde_avec_bezout(c, m)
    n, c, d = int(n), int(c), int(d)
    return (n, c), (n, d)


def chiffrer_message(cle_privee, message):
    """
    :param cle_privee
    :type cle_privee: tuple
    :param message à chiffrer
    :type message: str
    :return message chiffré
    """
    (n, c) = cle_privee
    # Conversion du message en ASCII
    message_ascii = [str(ord(caractere)) for caractere in message]
    # Vérification que chaque code ASCII ait bien une longueur de 3 digits en complétant par des 0
    for index, element in enumerate(message_ascii):
        if len(element) < 3:
            while len(element) < 3:
                element = '0' + element
            message_ascii[index] = element
    # Regroupement du message ascii
    message_ascii = ''.join(message_ascii)
    # Définition de la taille des blocs du message
    debut, fin = 0, 4
    # Ajout éventuel de zéros au message afin qu'il soit un multiple de la taille d'un bloc, içi 4
    while len(message_ascii) % fin != 0:
        message_ascii += '0'
    # Groupement
    groupes = []
    while fin <= len(message_ascii):
        groupes.append(message_ascii[debut:fin])
        debut = fin
        fin += 4
    # Chiffrement et retour des groupes
    return [str(((int(groupe)) ** c) % n) for groupe in groupes]

