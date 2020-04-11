import numpy as np


# récupération de la valeur au format hexadécimal
def recuperer_valeur_format_hexa():
    saisie = input("saisir la valeur: 0x")
    hexa = []
    for caractere in saisie:
        if caractere == '0':
            hexa.append(0)
            hexa.append(0)
            hexa.append(0)
            hexa.append(0)
        if caractere == '1':
            hexa.append(0)
            hexa.append(0)
            hexa.append(0)
            hexa.append(1)
        if caractere == '2':
            hexa.append(0)
            hexa.append(0)
            hexa.append(1)
            hexa.append(0)
        if caractere == '3':
            hexa.append(0)
            hexa.append(0)
            hexa.append(1)
            hexa.append(1)
        if caractere == '4':
            hexa.append(0)
            hexa.append(1)
            hexa.append(0)
            hexa.append(0)
        if caractere == '5':
            hexa.append(0)
            hexa.append(1)
            hexa.append(0)
            hexa.append(1)
        if caractere == '6':
            hexa.append(0)
            hexa.append(1)
            hexa.append(1)
            hexa.append(0)
        if caractere == '7':
            hexa.append(0)
            hexa.append(1)
            hexa.append(1)
            hexa.append(1)
        if caractere == '8':
            hexa.append(1)
            hexa.append(0)
            hexa.append(0)
            hexa.append(0)
        if caractere == '9':
            hexa.append(1)
            hexa.append(0)
            hexa.append(0)
            hexa.append(1)
        if caractere == 'A' or caractere == 'a':
            hexa.append(1)
            hexa.append(0)
            hexa.append(1)
            hexa.append(0)
        if caractere == 'B' or caractere == 'b':
            hexa.append(1)
            hexa.append(0)
            hexa.append(1)
            hexa.append(1)
        if caractere == 'C' or caractere == 'c':
            hexa.append(1)
            hexa.append(1)
            hexa.append(0)
            hexa.append(0)
        if caractere == 'D' or caractere == 'd':
            hexa.append(1)
            hexa.append(1)
            hexa.append(0)
            hexa.append(1)
        if caractere == 'E' or caractere == 'e':
            hexa.append(1)
            hexa.append(1)
            hexa.append(1)
            hexa.append(0)
        elif caractere == 'F' or caractere == 'f':
            hexa.append(1)
            hexa.append(1)
            hexa.append(1)
            hexa.append(1)
    return hexa


# récupération de la valeur au format binaire
def recuperer_valeur_format_binaire():
    saisie = input("saisir la valeur: 0b")
    binaire = []
    for caractere in saisie:
        if caractere == '1':
            binaire.append(1)
        elif caractere == '0':
            binaire.append(0)
    return binaire


# choix de la base pour saisie de la valeur
def recuperer_valeur():
    choix_base = input("Saisir 1 pour rentrer la valeurs au format binaire et 2 pour le format hexadecimal")
    if choix_base == '1':
        return recuperer_valeur_format_binaire()
    elif choix_base == '2':
        return recuperer_valeur_format_hexa()


# Traitement de la situation 1 (calcul et affichage du reste et affichage de T(x))
def traiter_situation_1():
    sx = recuperer_valeur()
    sx = np.array(sx)
    gx = np.array([1.0, 1.0])
    xd = np.array([1.0, 0.0])
    rx = np.polydiv(np.polymul(sx, xd), gx)[1][0]
    print("CRC: R(x)= ", int(rx))
    print("T(x)= " + str(np.concatenate((sx, np.array([int(i) for i in np.polydiv(np.polymul(sx, xd), gx)[0]])))))


# Traitement de la situation 2 (test des erreurs)
def traiter_situation_2():
    saisie = input("saisir T(x): ")
    tx = []
    for caractere in saisie:
        if caractere == '1':
            tx.append(1)
        elif caractere == '0':
            tx.append(0)
    tx = np.array(tx)
    gx = np.array([1.0, 1.0])
    reste = np.polydiv(tx, gx)[1][0]
    if reste == 0:
        print("Pas d'erreur, le reste vaut R(x)=0")
    else:
        print("Erreur, le reste vaut R(x)", reste)


# code pilote
choix = input("saisir 1 pour donner S(x) et calculer R(x)\nSaisir 2 pour donner T(x) et déterminer si il y a des erreurs ou non.\n\nVotre choix: ")
if choix == '1':
    traiter_situation_1()
elif choix == '2':
    traiter_situation_2()
