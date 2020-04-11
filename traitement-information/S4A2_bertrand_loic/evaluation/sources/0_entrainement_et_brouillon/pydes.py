import pyDes

# clé consituée de 8 octets
cle = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0")
# Chiffrement du message et complétion des caractères manquants par un espace pour atteindre un nombre de caractères multiple de la taille de la clé
donnees = cle.encrypt("Bonjour Monde !, ", ' ')
# Déchiffrement du message
print(cle.decrypt(donnees, ' '))
