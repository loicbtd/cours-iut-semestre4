# Projet : Problème du voyageur de commerce

Le projet est intégralement écrit en python 3.8 et il utilise les bibliothèques suivantes :

* prettytable
* glpk
* pylab-sdk
* numpy
* matplotlib
* progress

À priori, sous Linux, il suffit d'exécuter le makefile comme expliqué ci-dessous afin d'installer les bibliothèques python et lancer le programme.

Il faut néanmoins que le gestionnaire de paquet pip pour python 3 soit installé sur votre machine.

## Installer le projet


```shell
make install
```

## Lancer le programme
```shell
make run
```

## Utiliser le programme

La navigation se fait via la saisie de chiffres et à la touche Entrer

### Graphe sous format fichier

Vous pouvez ajouter ou supprimer des graphe dans le répertoire "donnee" du projet afin de les charger ensuite via le programme.

### Premier lancement

Le menu principal vous permet de choisir entre la génération aléatoire d'un graphe ou son chargement depuis un fichier.

Une fois qu'un graphe est généré ou chargé, deux options s'offrent à vous.

#### Option 1: Afficher le graphe

Cette option vous permet d'afficher le graphe.

#### Option 2: Afficher la matrice d'adjacence


Cette option permet d'afficher la matrice d'adjacence 

#### Option 2: Examiner l'influence du nombre et du type des configurations

La sélection de cette option vous tracera la courbe de la durée de vie du réseau en fonction du nombre de capteurs dans la configuration.

Ceci crée un nouveau fichier dans le répertoire "donnee" du projet dans lequel sera décrit la situation. Ce fichier pourra ensuite être rechargé pour une utilisation ultérieure.