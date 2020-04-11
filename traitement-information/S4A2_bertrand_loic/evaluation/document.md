# Récapitulatif des travaux pratiques de traitement de l'information

**Loïc BERTRAND - S4A2** 



## Tableau récapitulatif de toutes les réalisations

| Réalisation | Pourcentage d'aboutissement |
| :---------: | :-------------------------: |
|             |                             |

## Utilisation des outils

### Sha1sum

La commande sha1sum permet de calculer l'intégrité d'une donnée. Cela est par exemple utile dans le cadre d'un transfert de données. Dans ce cas on compare l'empreinte du fichier reçu avec l'empreinte du fichier avant l'envoi. Ci-dessous figure un exemple d'utilisation de cette commande.

```shell
#!/bin/sh

comparaison_des_empreintes(){
  echo "NOTICE: comparaison des empreintes"
  local empreinte1=$1
  local empreinte2=$2
  echo "NOTICE: empreinte1: $empreinte1"
  echo "NOTICE: empreinte2: $empreinte2"
  [ "$empreinte1" = "$empreinte2" ] \
    && echo "RESULTAT: empreintes identiques !" && return 0 \
    || echo "RESULTAT: empreintes différentes !" || return 1
}

FICHIER1="./fichier1"
FICHIER2="./fichier2"

printf "\n\n"

echo "**** Simulation d'un transfert de fichier avec succès****"
echo "NOTICE: génération du fichier 1"
touch $FICHIER1
echo "NOTICE: génération de l'empreinte du fichier1"
empreinte_fichier_1=$(sha1sum $FICHIER1 | cut --delimiter=' ' --field=1)
echo "NOTICE: simulation du transfert du fichier 1 vers le fichier 2."
cp $FICHIER1 $FICHIER2
echo "NOTICE: génération de l'empreinte du fichier2"
empreinte_fichier_2=$(sha1sum $FICHIER2 | cut --delimiter=' ' --field=1)
comparaison_des_empreintes $empreinte_fichier_1 $empreinte_fichier_2

printf "\n\n"

echo "**** Simulation d'un transfert de fichier avec échec****"
echo "NOTICE: génération du fichier 1"
touch $FICHIER1
echo "NOTICE: génération de l'empreinte du fichier1"
empreinte_fichier_1=$(sha1sum $FICHIER1 | cut --delimiter=' ' --field=1)
echo "NOTICE: simulation du transfert du fichier 1 vers le fichier 2."
cp $FICHIER1 $FICHIER2
echo "Bonjour Monde" > $FICHIER2
echo "NOTICE: génération de l'empreinte du fichier2"
empreinte_fichier_2=$(sha1sum $FICHIER2 | cut --delimiter=' ' --field=1)
comparaison_des_empreintes $empreinte_fichier_1 $empreinte_fichier_2
```

### PyDes

Le chiffrement DES (=Data Encryption Standart) est un un algorithme de chiffrement symétrique. Le module python pyDes permet de chiffrer et déchiffrer des messages comme le témoigne l'exemple ci-dessous.

```python
import pyDes

# clé consituée de 8 octets
cle = pyDes.des("DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0")
# Chiffrement du message et complétion des caractères manquants par un espace pour atteindre un nombre de caractères multiple de la taille de la clé
donnees = cle.encrypt("Bonjour Monde !, ", ' ')
# Déchiffrement du message
print(cle.decrypt(donnees, ' '))
```

### RSA

Le chiffrement RSA, du nom de ses trois inventeurs Ronald Rivest, Adi Shamir et Leonard Adleman, est un algorithme de chiffrement asymétrique. Le module python Crypto permet de générer une paire de clé. L'une est privée, l'autre publique.  Deux tiers peuvent ainsi échanger leurs clés publiques afin de communiquer de manière sécurisée. On peut utiliser ce module comme cela est décrit ci-dessous.

```python
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
```

### Gnupg

GPG de l'acronyme GNU Privacy Guard permet le chiffrement symétrique ou asymétrique ainsi que la signature de données. Dans l'exemple ci-dessous, on voit comment générer des clés.

```shell
#!/bin/sh

mkdir -p ./gpg
export GNUPGHOME="$(pwd)/gpg"
cat > fichier_temporaire << FIN
     %echo "Génération d'une clé GPG"
     Key-Type: DSA
     Key-Length: 1024
     Subkey-Type: ELG-E
     Subkey-Length: 1024
     Name-Real: Prénom Nom
     Name-Comment: commentaire
     Name-Email: exemple@exemple.fr
     Expire-Date: 0
     Passphrase: mot_de_passe
     %commit
     %echo "REUSSI"
FIN
gpg --batch --generate-key fichier_temporaire
gpg --list-secret-keys
rm fichier_temporaire
```

### Openssl

Openssl est un outil de chiffrement qui permet entre autres de générer des certificats SSL qui sont par exemple utiles pour sécuriser les échanges via le 44protocole https. Je l'utilise par exemple pour générer des certificats auto-signés pour mon reverse-proxy Nginx lorsque le robot de certification Let's Encrypt échoue dans la génération automatique de certificats SSL valides. Ci-dessous, voici comment générer un couple certificat / clé privé.

```shell
openssl req -x509 -nodes -days 3 -newkey rsa:4096 -keyout ./cle_privee.pem -out ./certificat.pem -subj "/C=FR/ST=State/L=Location/O=Organization/OU=Unit/CN=Name"
```

## Explication des algorithmes

