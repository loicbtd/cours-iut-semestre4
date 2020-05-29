# pip install pycryptodome pour obtenir les modules ci-dessous
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# Génération d'une paire de clé publique / clé privée de 512 bits
paire_cles = RSA.generate(1024)
cle_publique_rsa = PKCS1_OAEP.new(RSA.importKey(paire_cles.publickey().exportKey()))
cle_privee_rsa = PKCS1_OAEP.new(RSA.importKey(paire_cles.export_key()))

# Chiffrement du message avec la clé publique
message = "Hello Monde !"
print("Message: " + message)
message_chiffre = cle_publique_rsa.encrypt(str.encode(message))
print("Message chiffré: " + str(message_chiffre))

# Déchiffrement du message avec la clé privée
message_dechiffre = cle_privee_rsa.decrypt(message_chiffre)
print("Message déchiffré: " + str(message_dechiffre))

